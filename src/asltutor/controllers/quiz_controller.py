from asltutor.models.quiz import Quiz, Question
from flask import Blueprint
from flask import request, Response
from bson import ObjectId

quiz = Blueprint('quiz', __name__)


@quiz.route('/quiz', methods=['POST'])
def create_quiz():
    """

    Create a quiz
    request body

    :rtype: None
    """

    # check for json
    if request.content_type == 'application/json':
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
                        number_of_questions=len(ques),
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
            return Response('Failed: Content must be valid json', 400)
        return Response('Success ', 200)
    return Response('Failed: Content must be json', 202)


@quiz.route('/quiz', methods=['DELETE'])
def delete_quiz():
    """Delete an existing quiz in a module

    An admin can delete an existing quiz based on a given quiz Id

    query parameter: /quiz?qid=someObjectId
    no request body

    :rtype: none
    """
    qid = request.args.get('qid')
    if ObjectId.is_valid(qid):
        q = Quiz.objects.get_or_404(id=qid)
        for e in q.questions:
            e.delete()
        q.delete()
        return Response('Success', 200)
    return Response('Failed: invalid Id', 400)


@quiz.route('/quiz', methods=['PUT'])
def edit_quiz():
    """Edit an existing quiz

    An admin can edit an existing quiz givin a specific quiz Id.

    query parameter: /quiz?qid=someObjectId
    request body

    :rtype: None
    """
    qid = request.args.get('qid')
    q = Quiz.objects.get_or_404(id=qid)

    # check if request type is correct
    if request.content_type == 'application/json':
        r = request.get_json()

        return Response('Success', 200)
    return Response('Failed: Content must be json', 400)


@quiz.route('/quiz', methods=['GET'])
def get_quiz():
    """Get a quiz for a module

    Get a single quiz based on a given quiz Id

    query parameter: /quiz?qid=someObjectId
    no request body

    :rtype: json
    """
    # TODO: make an better serializer the JSON works better
    qid = request.args.get('qid')
    if ObjectId.is_valid(qid):
        quiz = Quiz.objects.get_or_404(id=qid)
        return Response(quiz.to_json(), 200, mimetype='application/json')
    return Response('Failed: invalid Id', 400)
