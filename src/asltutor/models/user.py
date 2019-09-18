from __future__ import absolute_import
from flask_login import UserMixin
from asltutor.database import db
from asltutor.models.module import Module
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
    public_id = db.StringField(max_length=50,unique=True)
    dob = db.DateTimeField(required=True)
    creation_date = db.DateTimeField()
    last_login = db.DateTimeField()
    email = db.EmailField(required=True)
    password = db.StringField(required=True)
    is_verified = db.BooleanField(default=False)
    completed_modules = db.ListField(
        db.EmbeddedDocumentField(Completed_Modules))

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.creation_date = datetime.now()

    def get_id(self):
        return self.id
