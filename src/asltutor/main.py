#!/usr/bin/env python3

from flask import Flask, render_template
from asltutor import settings, database, login_manager
import jwt
from mongoengine import *
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

app.config.from_object(settings.DevelopmentConfig)

# MongoDB
database.db.init_app(app)

# Flask Security
# not sure when this will actually end up used, for now using JWT
login_manager.lm.init_app(app)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/analytics')
def analytics():
    items = [
        { "word": "test", "url": "test.com", "times_requested": 42 }
    ]
    return render_template('analytics.html', items=items)

@app.route('/login')
def show_login():
    return render_template('login.html')

@app.route('/crowd-source')
def show_crowd_source():
    return render_template('crowd_sourcing.html')

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
