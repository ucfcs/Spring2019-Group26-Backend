from asltutor.models.module import Module
from asltutor.models.dictionary import Dictionary
from asltutor.models.quiz import Quiz
from flask import request, Response
from flask import Blueprint
from bson import ObjectId
from mongoengine.errors import NotUniqueError

module = Blueprint('module', __name__)


@module.route('/module/create', methods=['POST'])
def create_module():
    """Create a module

    An admin will be able to create a new learning module

    request body

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 415)

    r = request.get_json()

    # build and save the module
    try:
        mod = Module(module_name=r['module_name'], details=r['details'])
    except Exception as e:
        print(e)
        return Response('Failed: Bad request', 400)

    # save it so we have an Id to reference
    mod.save()

    # get the parent if it exists
    if 'parent' in r:
        err = Module.error_checker(id=r['parent'])
        # if parent id is wrong throw error
        if err:
            return err
        # else get parent object and add it to the new module
        parent = Module.objects.get(id=r['parent'])
        mod.parent = parent.id

        # if there is a child get the id of the child just in case we need to revert it
        if Module.objects(parent=r['parent']):
            old_id = Module.objects.get(parent=r['parent']).id

        # change the childs parent id to be the new module id
        Module.objects(parent=r['parent']).update_one(parent=mod.id)

    # if the user provided a list of words the verify them and add them to the module
    if 'words' in r:
        for i in r['words']:
            print("words")
            # a word id is wrong return error
            err = Dictionary.error_checker(i)
            if err:
                mod.delete()
                return err
            # get the word object and add it to the module word array
            word = Dictionary.objects.get(id=i)
            Module.objects(id=mod.id).update_one(push__words=word)

    # if the user provided a list of quizzes the verify them and add them to the module
    if 'quiz' in r:
        for i in r['quiz']:
            print("quiz")
            # a quiz id is wrong return error
            err = Quiz.error_checker(i)
            if err:
                mod.delete()
                return err
            quiz = Quiz.objects.get(id=i)
            Module.objects(id=mod.id).update_one(push__quiz=quiz)

    try:
        mod.save()
    except Exception as e:
        print(e)
        if old_id:
            Module.objects(parent=r['parent']).update_one(parent=old_id)

    # if a parent is not provided then the new module is the new head of the module list
    if 'parent' not in r:
        # find the module with no parent node and upsert parent to new modules id
        Module.objects(parent__exists=0).update_one(
            upsert=True, parent=mod.id)

    return Response('Success', 200)


@module.route('/module/addword', methods=['POST'])
def add_word():
    """Add a word to an existing module

    An admin will be able to add a word to an existing module

    request body

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 415)

    r = request.get_json()

    derr = Dictionary.error_checker(r['word_id'])
    merr = Module.error_checker(r['module_id'])
    if derr:
        return derr
    elif merr:
        return merr

    word = Dictionary.objects.get(id=r['word_id'])
    Module.objects(id=r['module_id']).update_one(push__words=word)
    return Response('Success', 200)


@module.route('/module/delete/id/<moduleId>', methods=['POST'])
def delete_module(moduleId):
    """Delete a module from the database

    Deletes the module and all of it quizzes from the database.
    Must also adjust the it's parents and/or children.

    :param moduleId: The Id of the module that an admin is deleting.
    :type submissionId: str

    :rtype: None
    """
    if not ObjectId.is_valid(moduleId):
        return Response('Failed: invalid Id', 400)

    o = Module.objects.get_or_404(id=moduleId)

    # link up the parents to the new children and vice versa.
    # if it has a parent
    if o.parent != None:
        # if it has a child
        if Module.objects(parent=o.id):
            # link parent to child
            Module.objects(parent=o.id).update(parent=o.parent)
    else:
        # if it does not have a parent meaning it's the first module
        Module.objects(parent=o.id).update(parent=None)

    # remove all quizzes for the module
    for e in o.quiz:
        e.delete()
    # delete the module
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
    if ObjectId.is_valid(moduleId) and Module:
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
