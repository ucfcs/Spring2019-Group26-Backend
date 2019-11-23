from asltutor.models.dictionary import Dictionary
from asltutor.models.submission import Submission
from asltutor.models.module import Module
from asltutor.models.user import User
from flask import Blueprint
from flask import request, Response
from bson import ObjectId
from asltutor import s3_helper
from werkzeug import secure_filename
from datetime import datetime

admin = Blueprint('admin', __name__)

# Everything in here should be privileged


@admin.route('/admin/stats', methods=['GET'])
def get_stats():
    """Get top most requested words

    Returns a list of JSON objects with the top 'N' where 5 <= N <= 100 most downloaded words.

    query parameter: /admin/stats?limit=somenumber
    where 5 <= somenumber <= 100

    no request body

    :rtype: json
    """
    limit = request.args.get('limit', None)
    if limit:
        limit = int(limit)
        if limit < 5 or limit > 100:
            limit = 20
    else:
        limit = 20

    o = Dictionary.objects(in_dictionary=False).order_by(
        '-times_requested')[:limit]
    return Response(o.to_json(), mimetype='application/json')


@admin.route('/admin/stats/users', methods=['GET'])
def get_user_stats():
    """Gets user stats

    Returns the following data points:
        total number of users
        total number of verified users
        total number of users registered within N number of days
        total number of users that logged within N number of days
        total number of submission
        total number of submissions created within N number of days
        average age of users

    no request body

    :rtype: json
    """
    num_users = User.objects.count()
    num_verified = User.objects().count()

    num_submission = Submission.objects.count()
    # avg_age = User.objects
    pass


@admin.route('/admin/submissions', methods=['GET'])
def get_submissions():
    """Get a list of all submissions filtered based on certian criteria.

    Returns an array of all submissions. It can be filtered based on quizId and/or moduleId and/or userId.
    For example, a user can request all of their sumissions for any combination of moduleId or quizId.
    Must have at least one filter otherwise error

    :query param submission: The Id of the submission that a user is requesting.
    :type submission_id: str
    :query param quiz: The quiz Id that a user wants all submissions for
    :type quiz: str
    :query param module: The module Id that a user wants all submissions for
    :type module: str
    :query param user: The username of the user that the admin wants all the submissions for
    :type user: str

    :rtype: JSON
    """

    # If we are given a submission Id no filtering needs to be done. Return the document referenced by the id.
    submissionId = request.args.get('submission', None)
    username = request.args.get('user', None)
    quizId = request.args.get('quiz', None)
    moduleId = request.args.get('module', None)

    if submissionId:
        err = Submission.error_checker(submissionId)
        if err:
            return err
         # submission cannot be combined with other queries
        elif username or quizId or moduleId:
            return Response('Failed: Submission query cannot be combined with other queries', 400)
        # submission id is corrent and no other queries have been specified
        else:
            return Response(Submission.objects.get(id=submissionId).to_json(), mimetype='application/json')

    # if submissionId is not specified do further filtering
    subs = Submission.objects()
    if not username and not quizId and not moduleId:
        return Response('Failed: specify at least one filter to view submissions', 412)

    if username:
        if User.objects(username=username):
            user = User.objects.get(username=username)
            subs = subs.filter(user_id=user.id)

    if moduleId:
        err = Module.error_checker(moduleId)
        if err:
            return Response(err)
        subs = subs.filter(module_id=moduleId)

    if quizId:
        err = Module.error_checker(quizId)
        if err:
            return Response(err)
        subs = Submission.objects(quiz_id=quizId)

    if subs:
        return Response(subs.order_by('-grade').to_json(), 200, mimetype='application/json')
    return Response('No content', 204)


@admin.route('/admin/dictionary', methods=['GET'])
def list_words():
    """Get a list of all words that have have not been approved yet.

    Returns a list of all word objects that have been uploaded to our crowdsorcing page
    but have not been approved

    :query param start: Where the user wants the list to start
    :type submission_id: int
    :query param limit: How many words the user wants per page
    :type quiz: int

    :rtype: JSON
    """

    start = request.args.get('start', None)
    if start:
        start = int(start)
        if start >= Dictionary.objects(in_dictionary=False, url__exists=1).count():
            start = 0
    else:
        start = 0

    limit = request.args.get('limit', None)
    if limit:
        limit = int(limit)
        if limit < 5 or limit > 100:
            limit = 20
    else:
        limit = 20

    return Response(Dictionary.objects(in_dictionary=False, url__exists=1).order_by('-word')[start:limit].to_json(), 200, mimetype='application/json')


@admin.route('/admin/dictionary', methods=['POST'])
def approve_word():
    """Approve words and make them publicly available

    Sets the in_dictionary value to true for the words sent

    request body

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 415)

    r = request.get_json()
    if 'word' not in r:
        return Response('Failed: invalid request', 400)

    if len(r['word']) == 0:
        return Response('Failed: no words provided', 400)

    for e in r['word']:
        Dictionary.objects(word=e).update(in_dictionary=True)

    return Response('Success, updated the dictionary', 200)


@admin.route('/admin/dictionary/delete', methods=['POST'])
def deny_word():
    """Deny words, remove the file from the S3 bucket and not the DB

    Deletes the specified word from the S3 bucket and removes the URL field for that word

    request body

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 415)

    r = request.get_json()
    if 'word' not in r:
        return Response('Failed: invalid request', 400)

    if len(r['word']) == 0:
        return Response('Failed: no words provided', 400)

    for e in r['word']:
        if Dictionary.objects(word=e):
            try:
                word = Dictionary.objects.get(word=e)
                if word.url == None:
                    return Response('Failed: word has no url field', 400)
                url = word.url
                word.update(unset__url=1)
                url = url.split('/')
                s3_helper.delete_file_from_s3(url[-1])
            except Exception as e:
                print(str(datetime.now()) + ' ', e)
                return Response('Failed: error deleting word', 501)
    return Response('Success: words deleted', 200)


@admin.route('/admin/dictionary/create', methods=['POST'])
def add_word():
    """Add a word to the dictionary

    Admins are able to add an ASL animation to our dictionary

    path parameter: /admin/dictionary/create
    request body

    :rtype: None
    """
    if 'file' not in request.files:
        return Response('Failed: missing file', 400)
    file = request.files['file']
    r = request.form.to_dict()
    """
        These attributes are also available

        file.filename
        file.content_type
        file.content_length
        file.mimetype

    """
    if file:
        file.filename = secure_filename(file.filename)
        w = enchant.Dict("en_US")
        word = ''.join(filter(str.isalpha, r['word'])).lower()
        # if it's an actual word try to upload the word
        if w.check(word):
            try:
                output = s3_helper.upload_file_to_s3(file)
                if Dictionary.objects(word=word):
                    Dictionary.objects(word=word).update_one(
                        url=output, in_dictionary=True)
                else:
                    Dictionary(word=word, url=output,
                               in_dictionary=True).save()
            except Exception as e:
                print(str(datetime.now()) + ' ', e)
                return Response('Failed: error uploading word', 501)
        else:
            return Response('Failed: word provided is not a vaild english word', 400)
    else:
        return redirect('/admin/create')
    return Response('Success', 200)
