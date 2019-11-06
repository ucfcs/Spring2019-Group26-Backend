from __future__ import absolute_import
from asltutor.database import db
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
        'queryset_class': QuerySet,
        'ordering': ['word']
    }


class Dictionary(Document):
    word = db.StringField(required=True, unique=True)
    url = db.URLField()
    in_dictionary = db.BooleanField(default=False)
    times_requested = db.IntField()

    def error_checker(id):
        if not ObjectId.is_valid(id):
            return Response('Failed: invalid Id', 400)

        if not Dictionary.objects(id=id):
            return Response('', 204)
