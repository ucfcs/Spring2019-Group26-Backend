from asltutor.models.quiz import Quiz, Question
from asltutor.models.module import Module
from asltutor.models.dictionary import Dictionary
from asltutor.models.submission import Submission, UserAnswers
from asltutor.models.user import User, Completed_Modules
from flask import Blueprint
from flask import request, Response
from bson import ObjectId

quiz = Blueprint('quiz', __name__)


@quiz.route('/module/quiz/id/<id_>', methods=['POST', 'GET'])
def create_or_get_quiz(id_):
    """
    POST:
        Create a quiz with no questions and attach it to a module

        path parameter: /module/quiz/id/<moduleId>
        request body

        :rtype: None
    GET:
        Get a quiz for a module

        Get a single quiz based on a given quiz Id

        path parameter: /module/quiz/id/<quizid>
        no request body

        :rtype: json
    """
    if not ObjectId.is_valid(id_):
        return Response('Failed: invalid Id', 400)

    if request.method == 'POST':
        if not Module.objects(id=id_):
            return Response('Failed: invalid module Id', 400)
        if request.content_type != 'application/json':
            return Response('Failed: Content-type must be application/json', 415)
        r = request.get_json()
        try:
            quiz = Quiz(quiz_name=r['quiz_name'], details=r['details'])
            quiz.save()
            ret = add_questions(quiz.id, r)
            if ret:
                quiz.delete()
                return ret
            Module.objects(id=id_).update_one(add_to_set__quiz=quiz)
        except:
            return Response('Failed: invalid request', 400)
        return Response('Success', 200)

    elif request.method == 'GET':
        quiz = Quiz.objects.get_or_404(id=id_)
        return Response(quiz.to_json(), 200, mimetype='application/json')


@quiz.route('/module/quiz/delete/id/<quizId>', methods=['POST'])
def delete_quiz(quizId):
    """Delete an existing quiz in a module

    An admin can delete an existing quiz based on a given quiz Id

    path parameter: /module/quiz/delete/id/<quizId>
    no request body

    :rtype: none
    """
    if not ObjectId.is_valid(quizId):
        return Response('Failed: invalid Id', 400)

    quiz = Quiz.objects.get_or_404(id=quizId)
    quiz.delete()
    return Response('Success', 200)


def add_questions(id_, r):
    if 'questions' not in r:
        return Response('Failed: no questions provided', 400)

    for e in r['questions']:
        if not ObjectId.is_valid(e['word']):
            return Response('Failed: invalid Id', 400)

        if not Dictionary.objects(id=e['word'], in_dictionary=True):
            return Response('', 204)

    for e in r['questions']:
        try:
            question = Question(
                question_text=e['question_text'], word=e['word'])
            question.save()
            Quiz.objects(id=id_).update_one(push__questions=question)
        except:
            return Response('Failed: invalid request', 400)


@quiz.route('/module/quiz/question/id/<id_>', methods=['POST', 'GET'])
def create_or_get_question(id_):
    """
    POST:
        Create a question and attach it to a quiz that is attached to a module

        path parameter: /module/quiz/question/id/<quizId>
        request body

        :rtype: None
    GET:
        Get a single question for a quiz

        path parameter: /module/quiz/question/id/<questionId>
        no request body

        :rtype: json
    """
    if not ObjectId.is_valid(id_):
        return Response('Failed: invalid Id', 400)

    if request.method == 'POST':
        if request.content_type != 'application/json':
            return Response('Failed: Content-type must be application/json', 415)
        r = request.get_json()

        ret = add_questions(id_, r)
        if ret:
            return ret
        else:
            return Response('Success', 200)

    elif request.method == 'GET':
        question = Question.objects.get_or_404(id=id_)
        return Response(question.to_json(), 200, mimetype='application/json')


@quiz.route('/module/quiz/question/delete/id/<questionId>', methods=['POST'])
def delete_question(questionId):
    """Delete an existing question in a quiz

    An admin can delete an existing question based on a given question Id

    path parameter: /module/quiz/question/delete/id/<questionId>
    no request body

    :rtype: none
    """
    if not ObjectId.is_valid(questionId):
        return Response('Failed: invalid Id', 400)

    question = Question.objects.get_or_404(id=questionId)
    question.delete()
    return Response('Success', 200)


def grade_and_verify(list, sub):
    count = 0
    answers = []
    hm = {}

    # make a hash map of the question objects
    quiz = Quiz.objects.get(id=sub.quiz_id.id)
    for e in quiz['questions']:
        hm[e.id] = e.word.word

    for i in list:
        # check if the oids are valid and exist
        err = Question.error_checker(i['question_id'])
        if err:
            return err

        # check if the question is on this quiz
        if ObjectId(i['question_id']) in hm:
            answers.append(UserAnswers(
                question_id=i['question_id'], user_answer=i['user_answer'], correct_answer=hm[ObjectId(i['question_id'])]))

            # check if the answer is right
            if i['user_answer'] == hm[ObjectId(i['question_id'])]:
                count += 1
        else:
            return Response('Failed: question id: {} is not a member of quiz: {}'.format(i['question_id'], quiz.quiz_name), 400)

    # grade the quiz
    num_questions = len(quiz['questions'])
    sub.grade = (count / num_questions) * 100
    sub.user_answers = answers
    return sub


@quiz.route('/module/quiz', methods=['POST'])
def submit_quiz():
    """Submit a quiz for a user

    request body

    :rtype: none
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 415)
    r = request.get_json()

    # check if the oids are valid and exist
    err = User.error_checker(r['user_id'])
    if err:
        return err
    err = Quiz.error_checker(id=r['quiz_id'])
    if err:
        return err
    err = Module.error_checker(id=r['module_id'])
    if err:
        return err

    # check if the quiz is part of the module
    if not Module.objects(id=r['module_id'], quiz=r['quiz_id']):
        return Response('Failed: quiz is not a member of module', 400)

    # if the module has a parent check to see if the user has completed it
    module = Module.objects.get(id=r['module_id'])
    if module.parent:
        if not User.objects(id=r['user_id'], completed_modules__module_id=module.parent):
            return Response('Failed: user has not completed the parent module', 403)

    # build submission object
    sub = Submission(user_id=r['user_id'],
                     quiz_id=r['quiz_id'], module_id=r['module_id'])

    # grade quiz
    sub = grade_and_verify(r['user_answers'], sub)

    # check for any errors in grading the quiz
    if isinstance(sub, Response):
        return sub

    # No errors so save the submission
    sub.save()

    # update the completed modules field
    if sub.grade >= 80:
        completed = True

        # check if the user has completed all the quizzes for the module
        for e in module.quiz:
            if not Submission.objects(user_id=r['user_id'], module_id=module.id, quiz_id=e.id, grade__gte=80):
                completed = False

        # If so and the module is not already marked as complete, mark it as complete
        if completed and not User.objects(id=r['user_id'], completed_modules__module_id=module.id):
            User.objects(id=r['user_id']).update(push__completed_modules=Completed_Modules(
                module_id=module.id, module_name=module.module_name))

    return Response(sub.to_json(), 200, mimetype='application/json')
