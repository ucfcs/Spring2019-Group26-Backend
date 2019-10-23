from __future__ import absolute_import
from asltutor.models.quiz import Quiz
from asltutor.models.dictionary import Dictionary
from asltutor.database import db
import flask_mongoengine as fm
import mongoengine_goodjson as gj
from mongoengine import PULL
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


class Module(Document):
    module_name = db.StringField(required=True, max_length=100, unique=True)
    details = db.StringField(max_length=500)
    parent = db.ObjectIdField(default=None)
    words = db.ListField(gj.FollowReferenceField(
        Dictionary, reverse_delete_rule=PULL))
    quiz = db.ListField(gj.FollowReferenceField(
        Quiz, reverse_delete_rule=PULL))

    def error_checker(id):
        if not ObjectId.is_valid(id):
            return Response('Failed: invalid Id', 400)

        if not Module.objects(id=id):
            return Response('', 204)
