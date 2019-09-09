from __future__ import absolute_import
from app.database import db
from mongoengine import CASCADE
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


class Quiz(Document):
    quiz_name = db.StringField(required=True, max_length=20)
    number_of_questions = db.IntField()
    details = db.StringField(max_length=500, required=True)
    questions = db.ListField(gj.FollowReferenceField('Question'))


class Question(Document):
    question_text = db.StringField(max_length=500)
    url = db.URLField()
    answer_bank = db.ListField(db.StringField(max_length=20))
    correct_index = db.IntField()
