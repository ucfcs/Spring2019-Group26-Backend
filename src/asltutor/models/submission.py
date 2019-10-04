from __future__ import absolute_import
from asltutor.database import db
from asltutor.models.user import User
from asltutor.models.quiz import Quiz, Question
from asltutor.models.module import Module
from mongoengine import CASCADE
from datetime import datetime
import flask_mongoengine as fm
import mongoengine_goodjson as gj
from flask import Response
from bson import ObjectId


class QuerySet(fm.BaseQuerySet, gj.QuerySet):
    """Queryset."""
    pass


class Document(db.Document, gj.Document):
    """Document."""
    meta = {
        'abstract': True,
        'queryset_class': QuerySet
    }


class UserAnswers(db.EmbeddedDocument):
    question_id = db.ReferenceField(Question, required=True)
    user_answer = db.StringField(required=True)


class Submission(Document):
    user_id = db.LazyReferenceField(
        User, required=True, reverse_delete_rule=CASCADE)
    quiz_id = db.LazyReferenceField(
        Quiz, required=True, reverse_delete_rule=CASCADE)
    module_id = db.LazyReferenceField(
        Module, required=True, reverse_delete_rule=CASCADE)
    user_answers = db.ListField(
        db.EmbeddedDocumentField(UserAnswers, required=True))
    grade = db.DecimalField(required=True, precision=2,
                            rounding='ROUND_HALF_UP', min_value=0, max_value=100)
    date_completed = db.DateTimeField()

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.date_completed = datetime.now()

    def error_checker(id):
        if not ObjectId.is_valid(id):
            return Response('Failed: invalid Id', 400)

        if not Submission.objects(id=id):
            return Response('', 204)
