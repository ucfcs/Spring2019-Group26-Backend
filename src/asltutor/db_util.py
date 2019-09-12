import mongoengine

"""
Used to add fake stuff to the database for testing.
Everything added will be in the correct format.
"""

# create DB and collections
# doesn't actually exist until it's filled with things
print("Creating the mongo client handle: myclient")
myclient = mongoengine.connect('asl', 'mongodb://localhost:27017/asl_tutor')
print("Creating the mongo database handle: asl")
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


def destroy_db(client=myclient):
    # check if the asl_tutor database exists and quit if it doesn't
    if "asl_tutor" not in client.list_database_names():
        print("The database does not exist.")
        return

    # checks if you ment to do that
    print("This will delete the mongo Database asl_tutor")
    if check():
        print("Scorched earth!!!")
        client.drop_database("asl_tutor")
        print("Existing databases: ")
        clinet.list_database_names()
    else:
        print("Quitting")


def add_users():
    pass


def add_modules(client):
    """
    Adds a single module to the module collection based on the following format:

    :param module_name: The module_name of this Module.  # noqa: E501
    :type module_name: str
    :param number_of_words: The number_of_words of this Module.  # noqa: E501
    :type number_of_words: int
    :param parent: The parent of this Module.  # noqa: E501
    :type parent: int
    :param child: The child of this Module.  # noqa: E501
    :type child: int
    :param words: The words of this Module.  # noqa: E501
    :type words: List[{
        :param word_id: The word_id of this ModuleWords.  # noqa: E501
        :type word_id: int
        :param word: The word of this ModuleWords.  # noqa: E501
        :type word: str
        :param url: The url of this ModuleWords.  # noqa: E501
        :type url: str
    }]
    :param quiz: The quiz of this Module.  # noqa: E501
    :type quiz: List[{
        :param quiz_id: The quiz_id of this ModuleQuiz.  # noqa: E501
        :type quiz_id: int
        :param quiz_name: The quiz_name of this ModuleQuiz.  # noqa: E501
        :type quiz_name: str
        :param number_of_questions: The number_of_questions of this ModuleQuiz.  # noqa: E501
        :type number_of_questions: int
    }]
    """

    # no parent or child was added because there is only one module
    words = ["test", "hello", "sick", "pizza", "botany"]
    add_list = [{"module_name": "Module One",
                 "number_of_words": 0, "words": words}]


def add_quizes():
    # q = Quiz(quiz_name='Test quiz', number_of_questions=5)
    # q.save()
    # ques1 = Question(quiz=q, question_text='Test question 1', url='http://test.com',
    #                  answer_bank=['answer1', 'answer2', 'answer3', 'answer4'], correct_index=2)
    # ques1.save()
    # ques2 = Question(quiz=q, question_text='Test question 2', url='http://foo.com',
    #                  answer_bank=['answer1', 'answer2', 'answer3', 'answer4'], correct_index=3)
    # ques2.save()
    # ques3 = Question(quiz=q, question_text='Test question 3', url='http://bar.com',
    #                  answer_bank=['answer1', 'answer2', 'answer3', 'answer4'], correct_index=4)
    # ques3.save()
    # ques4 = Question(quiz=q, question_text='Test question 4', url='http://hello.com',
    #                  answer_bank=['answer1', 'answer2', 'answer3', 'answer4'], correct_index=1)
    # ques4.save()
    # ques5 = Question(quiz=q, question_text='Test question 5', url='http://pizza.com',
    #                  answer_bank=['answer1', 'answer2', 'answer3', 'answer4'], correct_index=2)
    # ques5.save()
    # print(q.to_json())
    # questions = Question.objects(quiz=q)
    # print(questions.to_json())
    pass


def add_words(db=asl):
    """
    Adds words to the Dictionary collection based on the following format:

    :param word: The word of this Dictionary.
    :type word: str
    :param url: The url of this Dictionary.
    :type url: str
    :param in_dictionary: The in_dictionary of this Dictionary.
    :type in_dictionary: bool
    :param times_requested: The times_requested of this Dictionary.
    :type times_requested: int
    """
    add_list = [
        {"word": "test", "url": "http://test.com",
            "in_dictionary": False, "times_requested": 7},
        {"word": "hello", "url": "http://hello.com",
            "in_dictionary": True, "times_requested": 25},
        {"word": "sick", "url": "http://sick.com",
            "in_dictionary": True, "times_requested": 4},
        {"word": "pizza", "url": "http://pizza.com",
            "in_dictionary": True, "times_requested": 10},
        {"word": "botany", "url": "http://botany.com",
            "in_dictionary": False, "times_requested": 0}
    ]
    dictionary = db["dictionary"]
    dictionary.insert_many(add_list)

    # print out the collection
    for x in dictionary.find():
        print(x)
    print("Done")


def print_all(client=myclient, db=asl):
    print("All mongo databases")
    print(myclient.list_database_names(), "\n")
    print("All collections in asl_tutor")
    cols = db.list_collection_names()
    print(cols, "\n")
    print("Printting the contents of each collection")
    for i in cols:
        print(i)
        for j in db[i].find():
            print(j)
        print()

    print("Done")


def add_subs():
    pass
