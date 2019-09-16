#!/usr/bin/env python3

from asltutor.database import db
import argparse
from asltutor.models.module import Module
from asltutor.models.quiz import Quiz, Question
from asltutor.models.dictionary import Dictionary
from asltutor.models.submission import Submission, UserAnswers
from asltutor.models.user import User, Completed_Modules
from datetime import datetime
from passlib.hash import pbkdf2_sha256
import traceback
import pprint
import json

"""
Used to add fake stuff to the database for testing.
Everything added will be in the correct format.

usage:
chmod +x db_util.py
source asltutor/venv/bin/activate
./db_util.py -h

run deactivate to exit venv
"""

# create DB
# doesn't actually exist until it's filled with things
# print("Creating the mongo client handle: myclient")
myclient = db.connect('asl', host='mongodb://localhost:27017/asl_tutor')
# print("Creating the mongo database handle: asl")
asl = myclient['asl_tutor']

# Two step verification


def check():
    inn = None
    print("Are you sure? [y/N]:")
    while inn == None:
        inn = input()
        if inn.lower() == 'y':
            return True
        elif inn.lower() == 'n':
            return False
        else:
            print("Please enter [y/N]")
            inn = None


def destroy_db():
    # check if the asl_tutor database exists and quit if it doesn't
    if "asl_tutor" not in myclient.list_database_names():
        print("The database does not exist.")
        return

    # checks if you ment to do that
    print("This will delete the mongo Database asl_tutor")
    if check():
        print("Scorched earth!!!")
        myclient.drop_database("asl_tutor")
    else:
        print("Quitting")


def add_all():
    # adds words
    try:
        word_test = Dictionary(word='test', url='http://test.com',
                               in_dictionary=False, times_requested=7)
        word_hello = Dictionary(
            word='hello', url='http://hello.com', in_dictionary=True, times_requested=2)
        word_sick = Dictionary(word='sick', url='http://sick.com',
                               in_dictionary=False, times_requested=1)
        word_foo = Dictionary(word='foo', url='http://foo.com',
                              in_dictionary=True, times_requested=10)
        word_bar = Dictionary(word='bar', url='http://bar.com',
                              in_dictionary=True, times_requested=30)
        word_food = Dictionary(word='food', url='http://food.com',
                               in_dictionary=False, times_requested=5)
        word_goodbye = Dictionary(word='goodbye', url='http://goodbye.com',
                                  in_dictionary=True, times_requested=1)
        word_pizza = Dictionary(word='pizza', url='http://pizza.com',
                                in_dictionary=True, times_requested=7)
        word_hack = Dictionary(word='hack', url='http://hack.com',
                               in_dictionary=False, times_requested=30)
        word_computer = Dictionary(word='computer', url='http://computer.com',
                                   in_dictionary=False, times_requested=10)

        # import json
        # print(word_test.to_json())
        word_test.save()
        word_hello.save()
        word_sick.save()
        word_foo.save()
        word_bar.save()
        word_food.save()
        word_goodbye.save()
        word_pizza.save()
        word_hack.save()
        word_computer.save()

        q0 = Question(question_text='Sign for test', word=word_test)
        q1 = Question(question_text='Sign for hello', word=word_hello)
        q2 = Question(question_text='Sign for sick', word=word_sick)
        q3 = Question(question_text='Sign for foo', word=word_foo)
        q4 = Question(question_text='Sign for bar', word=word_bar)
        q5 = Question(question_text='Sign for food', word=word_food)
        q6 = Question(question_text='Sign for goodbye', word=word_goodbye)
        q7 = Question(question_text='Sign for pizza', word=word_pizza)
        q8 = Question(question_text='Sign for hack', word=word_hack)
        q9 = Question(question_text='Sign for computer', word=word_computer)

        q0.save()
        q1.save()
        q2.save()
        q3.save()
        q4.save()
        q5.save()
        q6.save()
        q7.save()
        q8.save()
        q9.save()

        quiz_1 = Quiz(quiz_name='Test quiz 1',
                      details='This is the first test quiz', questions=[q0, q1, q2, q3, q4])
        quiz_1.number_of_questions = len(quiz_1.questions)
        quiz_1.save()

        quiz_2 = Quiz(quiz_name='Test quiz 2',
                      details='This is the second test quiz', questions=[q5, q8, q9])
        quiz_2.number_of_questions = len(quiz_2.questions)
        quiz_2.save()

        quiz_3 = Quiz(quiz_name='Test quiz 3',
                      details='This is the third test quiz', questions=[q3, q5, q6, q7])
        quiz_3.number_of_questions = len(quiz_3.questions)
        quiz_3.save()

        quiz_4 = Quiz(quiz_name='Test quiz 4',
                      details='This is the forth test quiz', questions=[q6, q8])
        quiz_4.number_of_questions = len(quiz_2.questions)
        quiz_4.save()

        mod_1 = Module(module_name='Test module 1', details='This is the first module', words=[
                       word_computer, word_test, word_hello, word_sick, word_foo, word_bar, word_hack, word_food], quiz=[quiz_1, quiz_2])

        mod_2 = Module(module_name='Test module 2', details='This is the two module', words=[
                       word_foo, word_food, word_goodbye, word_pizza, word_hack], quiz=[quiz_3, quiz_4])

        mod_3 = Module(module_name='Test module 3', details='This is the three module', words=[
                       word_goodbye, word_hack], quiz=[quiz_4])

        mod_1.save()
        mod_2.save()
        mod_3.save()

        mod_3.parent = mod_2.id
        mod_3.number_of_words = len(mod_3.words)
        mod_3.save()

        mod_2.parent = mod_1.id
        mod_2.number_of_words = len(mod_2.words)
        mod_2.child = mod_3.id
        mod_2.save()

        mod_1.child = mod_2.id
        mod_1.number_of_words = len(mod_1.words)
        mod_1.save()

        user_1 = User(username='baba_yaga', firstname='jon', lastname='wick', dob='1964-09-02',
                      email='babayaga64@gmail.com', password=pbkdf2_sha256.hash('willkillugood'), last_login=str(datetime.now()))
        user_1.creation_date = '2019-09-13 15:47:18.171396'
        comp1 = Completed_Modules(
            module_id=mod_1.id, module_name=mod_1.module_name)

        user_1.completed_modules = [comp1]
        user_1.save()

        ans0 = UserAnswers(question_id=q0.id, user_answer=q0.word.word)
        ans1 = UserAnswers(question_id=q1.id, user_answer=q1.word.word)
        ans2 = UserAnswers(question_id=q2.id, user_answer=word_bar.word)
        ans3 = UserAnswers(question_id=q3.id, user_answer=q3.word.word)
        ans4 = UserAnswers(question_id=q4.id, user_answer=q4.word.word)
        sub_1 = Submission(user_id=user_1, quiz_id=quiz_1, module_id=mod_1, user_answers=[
                           ans0, ans1, ans2, ans3, ans4], grade=4)
        sub_1.save()
    except Exception:
        print("An error occured filling the database.")
        print("================== ERROR =====================")
        traceback.print_exc()
        print("==============================================")
        print("Cleaning up ...")
        myclient.drop_database("asl_tutor")
        print("Done")


def print_all():
    print("All mongo databases")
    print(myclient.list_database_names(), "\n")
    print("All collections in asl_tutor")
    cols = asl.list_collection_names()
    print(cols, "\n")
    print("Printting the contents of each collection")
    for i in cols:
        print(i)
        for j in asl[i].find():
            print(j)
        print()

    print("Done")


parser = argparse.ArgumentParser(
    description='A utility for adding dummy information into the mongo database. You\'re welcome.')

parser.add_argument(
    '-f', '--fill', help='Fills the database with dummy data', action='store_true')
parser.add_argument(
    '-d', '--destroy', help='Deletes all data and drops the database', action='store_true')
parser.add_argument(
    '-p', '--print', help='Print the entire contents of the database', action='store_true')

ppgroup = parser.add_argument_group(
    title='Pretty print', description='Used to pretty print a specific document for a collection. Automatically resolves reference fields.')
choices = ['dictionary', 'module', 'user', 'submission', 'question', 'quiz']
ppgroup.add_argument('-pp',
                     help='Pretty prints a specific document',  nargs=1, choices=choices, dest='pprint')
ppgroup.add_argument('-o',
                     help='Specify an object Id to pretty print', dest='ObjectId')


args = parser.parse_args()
if args.fill:
    add_all()
    print('Database filled')
elif args.print:
    print_all()
elif args.destroy:
    destroy_db()
elif args.pprint:
    try:
        if 'quiz' in args.pprint:
            pprint.pprint(json.loads(
                Quiz.objects.get(id=args.ObjectId).to_json()))
        elif 'question' in args.pprint:
            pprint.pprint(json.loads(
                Question.objects.get(id=args.ObjectId).to_json()))
        elif 'module' in args.pprint:
            pprint.pprint(json.loads(
                Module.objects.get(id=args.ObjectId).to_json()))
        elif 'user' in args.pprint:
            pprint.pprint(json.loads(
                User.objects.get(id=args.ObjectId).to_json()))
        elif 'submission' in args.pprint:
            pprint.pprint(json.loads(
                Submission.objects.get(id=args.ObjectId).to_json()))
        elif 'dictionary' in args.pprint:
            pprint.pprint(json.loads(
                Dictionary.objects.get(id=args.ObjectId).to_json()))
    except Exception as e:
        print(e)
