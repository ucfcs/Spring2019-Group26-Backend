from asltutor.models.dictionary import Dictionary
from flask_mongoengine import MongoEngine
from flask import request, Response
from flask import Blueprint
from asltutor import s3_helper
from werkzeug import secure_filename
from flask import render_template
import enchant

dictionary = Blueprint('dictionary', __name__)


@dictionary.route('/dictionary/create', methods=['POST'])
def add_word():
    """Add a word to the dictionary

    Admins are able to add an ASL animation to our dictionary

    path parameter: /dictionary/create
    request body

    :rtype: None
    """
    if 'file' not in request.files:
        return Response('Failed: missing file', 400)
    file = request.files['file']
    r = request.form.to_dict()
    """
        These attributes are also available

        file.filename
        file.content_type
        file.content_length
        file.mimetype

    """
    if file:
        file.filename = secure_filename(file.filename)
        w = enchant.Dict("en_US")
        word = ''.join(filter(str.isalpha, r['word'])).lower()
        # if it's an actual word try to upload the word
        if w.check(word):
            if(Dictionary.objects.get(word=word) == None):
                try:
                    output = s3_helper.upload_file_to_s3(file)
                    Dictionary(word=word, url=output, in_dictionary=False).save()
                except Exception as e:
                    print(e)
                    return Response('Failed: error uploading word', 501)
            else:
                return Response('Failed: Request for that word has been submitted. Please await admit approval', 400)
        else:
            return Response('Failed: word provided is not a vaild english word', 400)
    else:
        return redirect('/dictionary/create')
    return Response('Success', 200)


@dictionary.route('/dictionary/delete', methods=['POST'])
def delete_word():
    """Delete a word from the dictioary

    Admins are able to delete a whole word object and animation from the database

    query parameter: /dictionary/delete?input=someword
    no request body

    :rtype: None
    """
    input_ = request.args.get('input', None)
    if not input_:
        return Response('Word not found', 204)

    imput_ = ''.join(filter(str.isalpha, input_)).lower()
    if Dictionary.objects(word=input_):
        try:
            url = Dictionary.objects.get(word=input_).url
            url = url.split('/')
            s3_helper.delete_file_from_s3(url[-1])
            Dictionary.objects(word=input_).delete()
        except Exception as e:
            print(e)
            return Response('Failed: error deleting word', 501)
        return Response('Success: word deleted from the dictionary', 200)
    return Response('Word not found', 204)


@dictionary.route('/dictionary/<string:word>', methods=['GET', 'POST'])
def get_word(word):
    """
    GET:
        Get a word in the dictionary

        Returns a JSON response contianing the word document of the word requested

        path parameter: /dictionary/{word}
        no request body

        :rtype: JSON
    POST:
        Request that we add a word to our dictionary

        Increments the times requested counter for a word

        path parameter: /dictionary/{word}
        no request body

        :rtype: None
    """
    word = ''.join(filter(str.isalpha, word)).lower()

    if request.method == 'GET':
        o = Dictionary.objects.get_or_404(word=word, in_dictionary=True)
        return Response(o.to_json(), 200, mimetype='application/json')

    if request.method == 'POST':
        w = enchant.Dict("en_US")
        if w.check(word):
            if Dictionary.objects(word=word, in_dictionary=False):
                Dictionary.objects(word=word).update_one(
                    upsert=True, inc__times_requested=1)
            elif Dictionary.objects(word=word, in_dictionary=True):
                return Response('Failed: word already exists', 409)
            else:
                Dictionary(word=word, times_requested=1).save()
        else:
            return Response('Failed: word provided is not a vaild english word', 400)
        return Response('Success: request received', 200)


@dictionary.route('/dictionary', methods=['GET'])
def get_words():
    """Get all words in the dictionary

    Returns a JSON response contianing the word and id of all words in the db

    path parameter: /dictionary
    no request body

    :rtype: JSON
    """
    return Response(Dictionary.objects(in_dictionary=True).only('word').to_json(), 200, mimetype='application/json')
