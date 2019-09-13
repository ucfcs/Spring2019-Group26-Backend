from __future__ import absolute_import
from flask_login import UserMixin
from app.database import db
from app.models.module import Module
from datetime import datetime
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


class Completed_Modules(db.EmbeddedDocument):
    module_id = db.LazyReferenceField(Module)
    module_name = db.StringField(max_length=20)


class User(Document, UserMixin):
    username = db.StringField(required=True, max_length=20, unique=True)
    firstname = db.StringField(max_length=20)
    lastname = db.StringField(max_length=20)
    dob = db.DateTimeField(required=True)
    creation_date = db.DateTimeField()
    email = db.EmailField(required=True)
    password = db.StringField(required=True)
    is_verified = db.BooleanField(default=False)
    last_login = db.DateTimeField()
    completed_modules = db.ListField(
        db.EmbeddedDocumentField(Completed_Modules))

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.creation_date = datetime.now()

    def get_id(self):
        return self.id
