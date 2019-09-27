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
        return Response('Failed: Content must be json', 400)

    r = request.get_json()
    o = Module(**r)
    o.save()
    return Response('Success', 200)


@module.route('/module/delete', methods=['POST'])
def delete_module():
    """Delete a module from the database

    Deletes the module and all of it quizzes from the database.
    Must also adjust the it's parents and/or children. Can use
    either objectId or the module name

    query parameter: /module/delete?input=input
    input can be an objectId or a module name

    :rtype: None
    """
    input_ = request.args.get('input')
    if ObjectId.is_valid(input_):
        o = Module.objects.get_or_404(id=input_)
    else:
        o = Module.objects.get_or_404(module_name=input_)
        print(o.quiz)
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
