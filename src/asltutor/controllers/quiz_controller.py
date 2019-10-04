from asltutor.models.quiz import Quiz, Question
from asltutor.models.module import Module
from asltutor.models.dictionary import Dictionary
from asltutor.models.submission import Submission, UserAnswers
from asltutor.models.user import User
from flask import Blueprint
from flask import request, Response
from bson import ObjectId

quiz = Blueprint('quiz', __name__)

# deprecated
# @quiz.route('/module/quiz/id/<moduleId>', methods=['POST'])


def create_bulk(moduleId):
    """
    If you have a complete quiz pass it here and it will populate
    all the fields for the whole quiz

    Create a quiz
    path parameter: /module/quiz/id/<moduleId>
    request body

    :rtype: None
    """

    # check for json
    if request.content_type != 'application/json':
        return Response('Failed: Content-type must be application/json', 415)

    r = request.get_json()
    """
    Since questions are added first we check to make sure they are
    ALL vaild before saving them to the DB
    """
    ques = []
    try:
        for i in range(len(r['questions'])):
            j = r['questions'][i]
            q = Question(**j)
            q.validate()
            ques.append(q)
        """
        If we get here then all of the questions are correct so
        we save them to our DB so our quiz has something to reference
        """
        for e in ques:
            e.save()

        quiz = Quiz(quiz_name=r['quiz_name'],
                    details=r['details'], questions=ques)
        quiz.validate()
        """
        if we get here with no errors then we're good to save
        the quiz to our DB
        """
        quiz.save()
    except:
        """
        Something went wrong burn it down and return an error
        """
        for e in ques:
            e.delete()
        quiz.delete()
        return Response('Failed: invalid entires', 400)
        """
        Add the quiz to the correct module
        """
    Module.objects(id=moduleId).update_one(add_to_set__quiz=quiz)
    return Response('Success', 200)


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
            quiz = Quiz(**r)
            quiz.save()
            Module.objects(id=id_).update_one(add_to_set__quiz=quiz)
        except:
            return Response('Failed: invalid request', 400)
        return Response('Success', 200)

    elif request.method == 'GET':
        quiz = Quiz.objects.get_or_404(id=id_)
        return Response(quiz.to_json(), 200, mimetype='application/json')

    else:
        return Response('Failed: server error', 500)


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

        Get a single quiz based on a given quiz Id

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
        if not ObjectId.is_valid(r['word']):
            return Response('Failed: invalid Id', 400)

        word = Dictionary.objects.get_or_404(id=r['word'])

        try:
            question = Question(question_text=r['question_text'], word=word)
            question.save()
            Quiz.objects(id=id_).update_one(push__questions=question)
        except:
            return Response('Failed: invalid request', 400)
        return Response('Success', 200)

    elif request.method == 'GET':
        question = Question.objects.get_or_404(id=id_)
        return Response(question.to_json(), 200, mimetype='application/json')

    else:
        return Response('Failed: server error', 500)


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


def grade_and_verify(list):
    count = 0
    for i in list:
        if ObjectId.is_valid(i['question_id']):
            q = Question.objects.get(id=i['question_id'])
            if i['user_answer'] == q.word['word']:
                count += 1
        else:
            return Response('Failed: invalid question Id', 400)
    return (count / len(list)) * 100


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
    if not Module.objects(id=module.id, quiz=quiz):
        return Response('Failed: quiz is not a member of module', 400)

    # this is all kinda nightmare fuel but it works
    sub = Submission(user_id=user.id, quiz_id=quiz.id, module_id=module.id)
    sub.grade = grade_and_verify(r['user_answers'])
    answers = []
    for i in r['user_answers']:
        answers.append(UserAnswers(
            question_id=i['question_id'], user_answer=i['user_answer']))
    sub.user_answers = answers
    sub.save()
    return Response('Success', 200)
