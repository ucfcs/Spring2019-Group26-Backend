from __future__ import absolute_import
from asltutor.database import db
import flask_mongoengine as fm
import mongoengine_goodjson as gj
from asltutor.models.dictionary import Dictionary
from mongoengine import PULL
from mongoengine import CASCADE
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


class Question(Document):
    question_text = db.StringField(max_length=500)
    word = gj.FollowReferenceField(Dictionary, reverse_delete_rule=CASCADE)

    def error_checker(id):
        if not ObjectId.is_valid(id):
            return Response('Failed: invalid Id', 400)

        if not Question.objects(id=id):
            return Response('Failed: quiestion object does not exist', 204)


class Quiz(Document):
    quiz_name = db.StringField(required=True, max_length=20)
    details = db.StringField(max_length=500, required=True)
    questions = db.ListField(gj.FollowReferenceField(
        Question, reverse_delete_rule=PULL))

    def error_checker(id):
        if not ObjectId.is_valid(id):
            return Response('Failed: invalid Id', 400)

        if not Quiz.objects(id=id):
            return Response('', 204)
