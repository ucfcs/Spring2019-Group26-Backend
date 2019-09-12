from asltutor.models.user import User
from asltutor import util, login_manager

from bson import ObjectId
from datetime import date, datetime


def create_user(body):
    """Create user

    Create and register a new user

    :param body: Creates a new user object
    :type body: dict | bytes

    :rtype: None
    """
    pass


def delete_user():
    """Delete a user

    Delete a the specified user and all information corresponding to that user from the database.

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

def login_user():
    """Logs user into the system

    :param body:
    :type body: dict | bytes

    :rtype: str
    """
    pass


def logout_user():
    """Logs out current logged in user session

    :rtype: None
    """
    pass
