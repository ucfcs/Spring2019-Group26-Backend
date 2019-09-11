#!/usr/bin/env python3

from flask import Flask
from app import settings, database, login_manager
from mongoengine import *


app = Flask(__name__)

app.config.from_object(settings.DevelopmentConfig)

# MongoDB
database.db.init_app(app)

# Flask Security
login_manager.lm.init_app(app)


@app.route('/')
def hello():
    return 'hello world'

# Auth
# Dictionary
# Module
# Quiz
# Question
# Submission
# User


def set_up_blueptints():
    from app.controllers.dictionary_controller import dictionary
    app.register_blueprint(dictionary, url_prefix='/v1')

    # from app.controllers.user_controller import user
    # app.register_blueprint(user, url_prefix='/v1')

    from app.controllers.quiz_controller import quiz
    app.register_blueprint(quiz, url_prefix='/v1')

    from app.controllers.stats_controller import stats
    app.register_blueprint(stats, url_prefix='/v1')

    from app.controllers.module_controller import module
    app.register_blueprint(module, url_prefix='/v1')


def run():
    set_up_blueptints()
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    run()
