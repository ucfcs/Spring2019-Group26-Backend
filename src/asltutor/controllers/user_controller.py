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
        return Response('Failed: Content must be json', 400)

    r = request.get_json()
    newUser = User(**r)
    try:
        newUser.save()
    except NotUniqueError as e:
        for field in User._fields:
            if field in str(e):
                return Response('Failed: field {} is already taken'.format(field), 409)
    return Response('Success', 200)


def delete_user():
    """Delete a user

    Delete the specified user and all information corresponding to that user from the database.

    :param username: The username of the user to be deleted
    :type username: str

    :rtype: None
    """
    pass


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


def get_user_info():
    """Get user info

    Get all user information for a user

    :param username: The username of the user to be fetched
    :type username: str

    :rtype: User
    """
    pass


@user.route('/user/login', methods=['POST'])
def login():
    """Logs user into the system

    :param body:
    :type body: dict | bytes

    :rtype: str
    """
    if request.is_json is None:
        return Response('Failed: Content must be json', 400)
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


@user.route('/user/<username>/submssions/<submissionId>', methods=['GET'])
def get_submission(submissionId):
    """View a submission given a specific submission Id

    Returns a single submission specified by a submission Id to a user.
    Validates whether or not the user has the correct privilege to view the submission.

    :param submissionId: The Id of the submission that a user is requesting.
    :type submission_id: str

    :rtype: JSON
    """
    if ObjectId.is_valid(submissionId):
        return Response(Submission.objects.get_or_404(id=submissionId).to_json(), mimetype='application/json')
    return Response('Failed: invalid Id', 400)


@user.route('/user/<username>/submissions', methods=['GET'])
def get_submissions(username):
    """Get a list of all submissions filtered based on certian criteria.

    Returns an array of all submissions. It can be filtered based on quizId and/or moduleId and/or userId.
    For example, a user can request all of their sumissions for any combination of moduleId or quizId.
    Defaults to all submissions for a user

    :query param quiz: The quiz Id that a user wants all submissions for
    :type quiz_id: str
    :query param moduleid: The module Id that a user wants all submissions for
    :type module_id: str

    :rtype: JSON
    """
    quizId = request.args.get('quiz', None)
    moduleId = request.args.get('module', None)
    user = User.objects.get(username=username)

    subs = Submission.objects(user_id__exact=user.id)
    if moduleId and ObjectId.is_valid(moduleId):
        subs = subs.filter(module_id__exact=moduleId)

    if quizId and ObjectId.is_valid(quizId):
        subs = Submission.objects(quiz_id__exact=quizId)
    return Response(subs.to_json(), mimetype='application/json')
