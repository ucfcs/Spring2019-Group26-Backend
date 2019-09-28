from asltutor.models.module import Module
from flask import request, Response
from flask import Blueprint
from bson import ObjectId

module = Blueprint('module', __name__)


@module.route('/module/create', methods=['POST'])
def create_module():
    """Create a module

    An admin will be able to create a new learning module

    request body

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 401)

    r = request.get_json()
    o = Module(**r)
    o.save()
    return Response('Success', 200)


@module.route('/module/addword', methods=['POST'])
def add_word():
    """Add a word to an existing module

    An admin will be able to add a word to an existing module

    request body

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 401)

    r = request.get_json()

    if not ObjectId.is_valid(r['word_id']) or not ObjectId.is_valid(r['module_id']):
        return Response('Failed: invalid Id', 400)

    word = Module.objects.get_or_404(id=r['word_id'])
    try:
        Module.objects(id=r['module_id']).update_one(push__words=word)
    except:
        return Response('Failed: module does not exist', 404)
    return Response('Success', 200)


@module.route('/module/delete/id/<moduleId>', methods=['POST'])
def delete_module(moduleId):
    """Delete a module from the database

    Deletes the module and all of it quizzes from the database.
    Must also adjust the it's parents and/or children. Can use
    either objectId or the module name

    :param moduleId: The Id of the module that an admin is deleting.
    :type submissionId: str

    :rtype: None
    """
    if not ObjectId.is_valid(moduleId):
        return Response('Failed: invalid Id', 400)

    o = Module.objects.get_or_404(id=moduleId)

    # link up the parents to the new children and vice versa.
    # Unlink if no parents or children exist.
    if o.parent != None:
        if o.child != None:
            # parent exists, child exists
            Module.objects(id=o.parent).update_one(child=o.child)
            Module.objects(id=o.child).update_one(parent=o.parent)
        else:
            # parent exists, child does not exist
            Module.objects(id=o.parent).update_one(unset__child)
    else:
        # parent does not exist, child exists
        Module.objects(id=o.child).update_one(unset__parent)

    for e in o.quiz:
        e.delete()
    o.delete()
    return Response('Success', 200)


@module.route('/module/id/<moduleId>', methods=['GET'])
def get_module(moduleId):
    """Get a specific module

    Get a single module givin a module Id

    path parameter: /module/id/<objectId>
    no request body

    :rtype: json
    """
    if ObjectId.is_valid(moduleId):
        return Response(Module.objects.get_or_404(id=moduleId).to_json(), mimetype='application/json')
    return Response('Failed: invalid Id', 400)


@module.route('/module', methods=['GET'])
def get_all_modules():
    """
    Get a list of all modules available to the user.
    Excludes word and quiz lists to limit the response size.
    Ment to be used to get top level info about all modules.

    :rtype: json
    """
    return Response(Module.objects.exclude('words', 'quiz').to_json(), mimetype='application/json')
