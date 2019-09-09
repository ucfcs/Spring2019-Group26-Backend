from __future__ import absolute_import
from flask_login import UserMixin
from app.database import db
from app.models.module import Module
from datetime import datetime


class Completed_Modules(db.EmbeddedDocument):
    module_id = db.LazyReferenceField(Module)
    module_name = db.StringField(max_length=20)


class User(db.Document, UserMixin):
    username = db.StringField(required=True, max_length=20)
    firstname = db.StringField(max_length=20)
    lastname = db.StringField(max_length=20)
    dob = db.DateTimeField(required=True)
    creation_date = db.DateTimeField()
    last_login = db.DateTimeField()
    email = db.EmailField(required=True)
    password = db.StringField(required=True)
    is_verified = db.BooleanField(default=False)
    completed_modules = db.ListField(
        db.EmbeddedDocumentField(Completed_Modules))

    def __init__(self, creation_date, username):
        self.creation_date = datetime.utcnow()
        self.username = username
