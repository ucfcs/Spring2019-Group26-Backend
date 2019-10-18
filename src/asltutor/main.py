#!/usr/bin/env python3
from flask import Response
from flask import Flask
from asltutor import settings, database
import jwt
from mongoengine import *
from flask_swagger_ui import get_swaggerui_blueprint
from flask import request, Response

DEV = True

app = Flask(__name__)

if DEV:
    app.config.from_object(settings.DevelopmentConfig)
else:
    app.config.from_object(settings.ProductionConfig)

# MongoDB
database.db.init_app(app)


@app.route('/')
def hello():
    return Response('Success: hello world', 200)

# Dictionary
# Module
# Quiz
# Question
# Submission
# User


"""
Swagger docs
"""

SWAGGER_URL = '/v1/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'ASLTutor docs'
    })

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

from asltutor.controllers.dictionary_controller import dictionary
app.register_blueprint(dictionary, url_prefix='/v1')

from asltutor.controllers.user_controller import user
app.register_blueprint(user, url_prefix='/v1')

from asltutor.controllers.quiz_controller import quiz
app.register_blueprint(quiz, url_prefix='/v1')

from asltutor.controllers.admin_controller import admin
app.register_blueprint(admin, url_prefix='/v1')

from asltutor.controllers.module_controller import module
app.register_blueprint(module, url_prefix='/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
