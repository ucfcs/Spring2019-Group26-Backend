from asltutor.models.quiz import Quiz, Question
from asltutor.models.module import Module
from asltutor.models.dictionary import Dictionary
from asltutor.models.submission import Submission, UserAnswers
from asltutor.models.user import User
from flask import Blueprint
from flask import request, Response
from bson import ObjectId

quiz = Blueprint('quiz', __name__)


@quiz.route('/module/quiz/id/<moduleId>', methods=['POST'])
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
        return Response('Failed: Content must be valid json', 400)

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


@quiz.route('/module/quiz/create/id/<moduleId>', methods=['POST'])
def create_quiz(moduleId):
    """
    Create a quiz with no questions and attach it to a module

    path parameter: /module/quiz/create/id/<moduleId>
    request body

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content must be valid json', 400)
    r = request.get_json()
    try:
        quiz = Quiz(**r)
        quiz.save()
        Module.objects(id=moduleId).update_one(add_to_set__quiz=quiz)
    except:
        return Response('Failed: invalid request', 400)
    return Response('Success', 200)


@quiz.route('/module/quiz/question/create/id/<quizId>', methods=['POST'])
def create_question(quizId):
    """
    Create a question and attach it to a quiz that is attached to a module

    path parameter: /module/quiz/question/create/id/<quizId>
    request body

    :rtype: None
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content must be valid json', 400)
    r = request.get_json()
    if not ObjectId.is_valid(r['word']):
        return Response('Failed: invalid Id', 400)

    word = Dictionary.objects.get_or_404(id=r['word'])

    try:
        question = Question(question_text=r['question_text'], word=word)
        question.save()
        Quiz.objects(id=quizId).update_one(add_to_set__questions=question)
    except:
        return Response('Failed: invalid request', 400)
    return Response('Success', 200)


@quiz.route('/module/quiz/delete/id/<quizId>', methods=['POST'])
def delete_quiz(quizId):
    """Delete an existing quiz in a module

    An admin can delete an existing quiz based on a given quiz Id

    path parameter: /module/quiz/delete/id/<quizId>
    no request body

    :rtype: none
    """
    if ObjectId.is_valid(quizId):
        quiz = Quiz.objects.get_or_404(id=quizId)
        quiz.delete()
        return Response('Success', 200)
    return Response('Failed: invalid Id', 400)


@quiz.route('/module/quiz/question/delete/id/<questionId>', methods=['POST'])
def delete_question(questionId):
    """Delete an existing question in a quiz

    An admin can delete an existing question based on a given question Id

    path parameter: /module/quiz/question/delete/id/<questionId>
    no request body

    :rtype: none
    """
    if ObjectId.is_valid(questionId):
        question = Question.objects.get_or_404(id=questionId)
        question.delete()
        return Response('Success', 200)
    return Response('Failed: invalid Id', 400)


@quiz.route('/module/quiz/id/<quizId>', methods=['GET'])
def get_quiz(quizId):
    """Get a quiz for a module

    Get a single quiz based on a given quiz Id

    path parameter: /module/quiz/id/<objectid>
    no request body

    :rtype: json
    """
    if ObjectId.is_valid(quizId):
        quiz = Quiz.objects.get_or_404(id=quizId)
        return Response(quiz.to_json(), 200, mimetype='application/json')
    return Response('Failed: invalid Id', 400)


@quiz.route('/module/quiz/question/id/<questionId>', methods=['GET'])
def get_question(questionId):
    """Get a single question for a quiz

    Get a single quiz based on a given quiz Id

    path parameter: /module/quiz/question/id/<objectid>
    no request body

    :rtype: json
    """
    if ObjectId.is_valid(questionId):
        question = Question.objects.get_or_404(id=questionId)
        return Response(question.to_json(), 200, mimetype='application/json')
    return Response('Failed: invalid Id', 400)


def grade_and_verify(list):
    count = 0
    for i in list:
        if ObjectId.is_valid(i['question_id']):
            q = Question.objects.get(id=i['question_id'])
            if i['user_answer'] == q.word['word']:
                count += 1
        else:
            return Response('Failed: invalid question Id', 400)
    return count


@quiz.route('/module/quiz', methods=['POST'])
def submit_quiz():
    """Submit a quiz for a user

    request body

    :rtype: none
    """
    if request.content_type != 'application/json':
        return Response('Failed: Content must be valid json', 400)
    r = request.get_json()

    # if this fails either the oids are invalid or the entries do not exist
    try:
        user = User.objects.get(id=r['user_id'])
        quiz = Quiz.objects.get(id=r['quiz_id'])
        module = Module.objects.get(id=r['module_id'])
    except:
        return Response('Failed: invalid Id(s)', 400)

    # this is all kinda nightmare fuel but it works
    sub = Submission(user_id=user.id, quiz_id=quiz.id, module_id=module.id)
    sub.grade = grade_and_verify(r['user_answers'])
    answers = []
    ans = r['user_answers']
    for i in r['user_answers']:
        answers.append(UserAnswers(
            question_id=i['question_id'], user_answer=i['user_answer']))
    sub.user_answers = answers
    sub.save()
    return Response('Success', 200)
