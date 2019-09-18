from asltutor.models.user import User
from asltutor import login_manager
from flask import current_app as app
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
                return Response('Failed: field {} is already taken'.format(field), 400)
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
