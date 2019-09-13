from __future__ import absolute_import
from asltutor.models.quiz import Quiz
from asltutor.models.dictionary import Dictionary
from asltutor.database import db
import flask_mongoengine as fm
import mongoengine_goodjson as gj


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
    module_name = db.StringField(required=True, max_length=20, unique=True)
    details = db.StringField(max_length=500)
    number_of_words = db.IntField()
    parent = db.ObjectIdField()
    child = db.ObjectIdField()
    words = db.ListField(gj.FollowReferenceField(Dictionary))
    quiz = db.ListField(gj.FollowReferenceField(Quiz))
