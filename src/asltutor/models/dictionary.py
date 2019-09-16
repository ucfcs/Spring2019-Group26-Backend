from __future__ import absolute_import
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


class Dictionary(Document):
    word = db.StringField(required=True, unique=True)
    url = db.URLField(unique=True)
    in_dictionary = db.BooleanField(default=False)
    times_requested = db.IntField()
