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
from datetime import datetime

user = Blueprint('user', __name__)


@user.route('/user/create', methods=['POST'])
def create_user():
    """Create user

    Create and register a new user

    :param body: Creates a new user object
    :type body: dict | bytes

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 415)

    r = request.get_json()
    # kind of a lot of if statements but I feel like this is more consistent
    # and gives more useful debugging information that just default invalid request
    if 'username' not in r:
        return Response('Failed: Please provide a username', 400)
    username = ''.join(filter(str.isalpha, r['username']))
    if 'dob' not in r:
        return Response('Failed: Please provide a dob', 400)
    if User.objects(username=username):
        return Response('Failed: username already exists', 409)
    newUser = User(username=username, dob=r['dob'])
    if 'firstname' not in r:
        return Response('Failed: Please provide a firstname', 400)
    newUser.firstname = r['firstname']
    if 'lastname' not in r:
        return Response('Failed: please provide a lastname', 400)
    newUser.lastname = r['lastname']
    try:
        newUser.save()
    except Exception as e:
        print(str(datetime.now()) + ' ' , e)
        return Response('Failed: invalid request', 400)
    return Response('Success: user added', 200)


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
    user = User.objects.get_or_404(username=username)
    return Response(user.to_json())


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
        err = Submission.error_checker(submissionId)
        if err:
            return err
        # submission cannot be combined with other queries
        elif quizId or moduleId:
            return Response('Failed: Submission query cannot be combined with other queries', 400)
        # submission id is corrent and no other queries have been specified
        else:
            return Response(Submission.objects.get(id=submissionId).to_json(), 200, mimetype='application/json')

    # if submissionId is not specified do further filtering
    user = User.objects.get_or_404(username=username)

    subs = Submission.objects(user_id=user.id)
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
