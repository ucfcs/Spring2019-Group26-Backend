from __future__ import absolute_import
from asltutor.database import db
from asltutor.models.user import User
from asltutor.models.quiz import Quiz, Question
from asltutor.models.module import Module
from mongoengine import CASCADE


class UserAnswers(db.EmbeddedDocument):
    question_id = db.ReferenceField(Question, required=True)
    user_answer = db.IntField(required=True)


class Submission(db.Document):
    user_id = db.LazyReferenceField(
        User, required=True, reverse_delete_rule=CASCADE)
    quiz_id = db.LazyReferenceField(
        Quiz, required=True, reverse_delete_rule=CASCADE)
    module_id = db.LazyReferenceField(
        Module, required=True, reverse_delete_rule=CASCADE)
    user_answers = db.EmbeddedDocumentField(UserAnswers, required=True)
    grade = db.IntField(required=True)
    date_completed = db.DateTimeField(required=True)
