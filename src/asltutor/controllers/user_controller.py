from asltutor.models.user import User
from asltutor.models.submission import Submission
from flask_mongoengine import MongoEngine
from bson import ObjectId
import datetime
from flask import request, Response, jsonify
from flask import Blueprint
from passlib.hash import pbkdf2_sha256
from flask_login import login_user
import jwt
from mongoengine.errors import NotUniqueError


user = Blueprint('user', __name__)


@user.route('/user/create', methods=['POST'])
def create_user():
    """Create user

    Create and register a new user

    :param body: Creates a new user object
    :type body: dict | bytes

    :rtype: None
    """
    if request.is_json is None:
        return Response('Failed: Content-type must be application/json', 415)

    r = request.get_json()
    newUser = User(**r)
    try:
        newUser.save()
    except NotUniqueError as e:
        for field in User._fields:
            if field in str(e):
                return Response('Failed: field {} is already taken'.format(field), 409)
    return Response('Success', 200)


@user.route('/user/<string:username>', methods=['POST'])
def delete_user(username):
    """Delete a user

    Delete the specified user and all information corresponding to that user from the database.

    :path param username: The username of the user to be deleted
    :type username: str

    :rtype: None
    """
    user = User.objects.get_or_404(username=username)
    user.delete()
    return Response('Success: user has been deleted')


def edit_user():
    """Edit a user

    Edits a users information

    :param body: Updated user object
    :type body: dict | bytes
    :param username: The username of the user to be edited
    :type username: str

    :rtype: None
    """
    pass


@user.route('/user/<string:username>', methods=['GET'])
def get_user_info(username):
    """Get user info

    Get all user information for a user

    :param username: The username of the user to be fetched
    :type username: str

    :rtype: json
    """
    print(username)

    if User.objects(username=username):
        return Response(User.objects(username=username).exclude('password', 'last_login', 'is_active').to_json())
    return Response('Failed: User not found', 404)


@user.route('/user/login', methods=['POST'])
def login():
    """Logs user into the system

    :param body:
    :type body: dict | bytes

    :rtype: str
    """
    if request.is_json is None:
        return Response('Failed: Content-type must be application/json', 415)
    content = request.get_json()
    username = content['username']
    password = content['password']
    isUser = User.objects.get(username=username)
    # validation, is this a valid user and is this their password
    if not isUser and not pbkdf2_sha256.verify(password, isUser.password):
        return Response('Failed: Credentials are wrong', 400)
    # return a JWT token if they are validated
    token = jwt.encode({'public_id': isUser.get_id(), 'exp': datetime.datetime.utcnow(
    ) + datetime.timedelta(days=7)}, app.config['SECRET_KEY'])
    isUser.last_login = datetime.datetime.now()
    isUser.save()
    return jsonify({'token': token.decode('UTF-8')})


def logout_user():
    """Logs out current logged in user session

    :rtype: None
    """
    pass


@user.route('/user/<string:username>/submissions', methods=['GET'])
def get_submissions(username):
    """Get a list of all submissions filtered based on certian criteria.

    Returns a single submission specified by a submission Id to a user.
    or
    Returns an array of all submissions. It can be filtered based on quizId and/or moduleId and/or userId.
    For example, a user can request all of their sumissions for any combination of moduleId or quizId.
    Defaults to all submissions for a user

    :query param submission: The Id of the submission that a user is requesting.
    :type submission_id: str
    :query param quiz: The quiz Id that a user wants all submissions for
    :type quizId: str
    :query param moduleId: The module Id that a user wants all submissions for
    :type moduleId: str

    :rtype: JSON
    """

    # If we are given a submission Id no filtering needs to be done. Return the document referenced by the id.
    submissionId = request.args.get('submission', None)
    quizId = request.args.get('quiz', None)
    moduleId = request.args.get('module', None)
    if submissionId:
        if ObjectId.is_valid(submissionId):
            # submission cannot be combined with other queries
            if not quizId and not moduleId:
                return Response(Submission.objects.get_or_404(id=submissionId).to_json(), mimetype='application/json')
            else:
                return Response('Failed: Submission query cannot be combined with other queries', 400)
        else:
            return Response('Failed: invalid Id', 400)

    # if submissionId is not specified do further filtering
    user = User.objects.get_or_404(username=username)

    subs = Submission.objects(user_id__exact=user.id)
    if moduleId:
        if ObjectId.is_valid(moduleId):
            subs = subs.filter(module_id__exact=moduleId)
        else:
            return Response('Failed: invalid Id', 400)

    if quizId:
        if ObjectId.is_valid(quizId):
            subs = Submission.objects(quiz_id__exact=quizId)
        else:
            return Response('Failed: invalid Id', 400)

    if subs:
        return Response(subs.to_json(), mimetype='application/json')
    return Response('Failed: No submission found for that query')
