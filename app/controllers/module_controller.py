from app.models.module import Module
from flask import request, Response
from flask import Blueprint
from bson import ObjectId

module = Blueprint('module', __name__)


@module.route('/module', methods=['POST'])
def create_module():
    """Create a module

    An admin will be able to create a new learning module

    request body

    :rtype: None
    """
    if request.content_type == 'application/json':
        r = request.get_json()
        o = Module(**r)
        o.number_of_words = len(r['words'])
        o.save()
        return Response('Success', 200)
    return Response('Failed: Content must be json', 400)


@module.route('/module', methods=['DELETE'])
def delete_module():
    """Delete a module from the database

    Deletes the module and all of it quizzes from the database.
    Must also adjust the it's parents and/or children. Can use
    either objectId or the module name

    query parameter: /module?input=input
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


@module.route('/module', methods=['PUT'])
def edit_module(body, module_id):  # noqa: E501
    """Edit an existing module

    An admin will be able to edit existing learning modules. # noqa: E501

    :param body: The module object that the admin wants to edit
    :type body: dict | bytes
    :param module_id: The module Id of the module a user wants.
    :type module_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = FullModule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


@module.route('/module', methods=['GET'])
def get_module():
    """Get a specific module

    Get a single module givin a module Id

    query parameter (optional): /module?oid=someObjectId
    no request body

    :rtype: json
    """
    # check if a specific object Id was provided
    if 'oid' in request.args:
        # get the module object given a specific module Id
        if ObjectId.is_valid(oid):
            return Response(Module.objects.get_or_404(id=oid).to_json(), mimetype='application/json')
        return Response('Failed: invalid Id', 400)

    # Otherwise get a list of all modules available to the user.
    # Excludes word and quiz lists to limit the response size.
    # Ment to be used to get top level info about all modules.
    else:
        return Response(Module.objects.exclude('words', 'quiz').to_json(), mimetype='application/json')
