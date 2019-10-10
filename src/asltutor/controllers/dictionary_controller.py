from asltutor.models.dictionary import Dictionary
from flask_mongoengine import MongoEngine
from flask import request, Response
from flask import Blueprint
from asltutor import s3_helper
from werkzeug import secure_filename
from flask import render_template

dictionary = Blueprint('dictionary', __name__)


@dictionary.route('/dictionary/create')
def create():
    return render_template('upload.html')


@dictionary.route('/dictionary/create', methods=['POST'])
def add_word():
    """Add a word to the dictionary

    Admins are able to add an ASL animation to our dictionary

    path parameter: /dictionary/create
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
    # TODO need to have admin validate the words
    if file:
        file.filename = secure_filename(file.filename)
        try:
            output = s3_helper.upload_file_to_s3(file)
            word = ''.join(filter(str.isalpha, r['word'])).lower()
            Dictionary(word=word, url=output, in_dictionary=True).save()
        except Exception as e:
            print(e)
            return Response('Failed: error', 500)
    else:
        return redirect('/dictionary/create')
    return Response('Success', 200)


@dictionary.route('/dictionary/delete', methods=['POST'])
def delete_word():
    """Delete a word from the dictioary

    Admins are able to delete a whole word object and animation from the database

    query parameter: /dictionary/delete?input=someword
    no request body

    :rtype: None
    """
    input_ = request.args.get('input', None)
    if not input_:
        return Response('Word not found', 204)

    imput_ = ''.join(filter(str.isalpha, input_)).lower()
    if Dictionary.objects(word=input_):
        try:
            url = Dictionary.objects.get(word=input_).url
            url = url.split('/')
            s3_helper.delete_file_from_s3(url[-1])
            Dictionary.objects(word=input_).delete()
        except Exception as e:
            print(e)
            return Response('Failed', 500)
        return Response('Success: word deleted from the dictionary', 200)
    return Response('Word not found', 204)


@dictionary.route('/dictionary/<string:word>', methods=['GET'])
def get_word(word):
    """Get a word in the dictionary

    Returns a JSON response contianing the word document of the word requested

    path parameter: /dictionary/word
    no request body

    :rtype: JSON
    """
    word = ''.join(filter(str.isalpha, word)).lower()
    if not Dictionary.objects(word=word):
        Dictionary(word=word, times_requested=1).save()
        return Response('Word not found', 404)

    o = Dictionary.objects.get(word=word)
    if o.in_dictionary == False:
        Dictionary.objects(word=word).update_one(
            upsert=True, inc__times_requested=1)
        return Response('Word not found', 204)

    return Response(o.to_json(), 200, mimetype='application/json')


@dictionary.route('/dictionary', methods=['GET'])
def get_words():
    """Get all words in the dictionary

    Returns a JSON response contianing the word and id of all words in the db

    path parameter: /dictionary
    no request body

    :rtype: JSON
    """
    start = request.args.get('start', None)
    if start:
        start = int(start)
        if start >= Dictionary.objects(in_dictionary=True).count():
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

    return Response(Dictionary.objects(in_dictionary=True)[start:limit].only('word').to_json(), 200, mimetype='application/json')


@dictionary.route('/dictionary/search', methods=['GET'])
def search_word():
    """Get search for a word in our database

    Returns a word object in a JSON response

    path parameter: /dictionary/search
    no request body

    :rtype: JSON
    """
    input_ = request.args.get('input', None)
    if not input_:
        return Response('Word not found', 204)

    input_ = ''.join(filter(str.isalpha, input_)).lower()
    o = Dictionary.objects(word__contains=input_)
    if o:
        return Response(o.to_json(), 200, mimetype='application/json')
    return Response('Word not found', 204)
