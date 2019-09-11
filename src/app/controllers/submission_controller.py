from app.models.submission import Submission


def get_submission():
    """View a submission given a specific submission Id

    Returns a single submission specified by a submission Id to a user or admin. Validates whether or not the user has the correct privilege to view the submission.

    :param submission_id: The Id of the submission that a user is requesting.
    :type submission_id: str

    :rtype: Submission
    """
    pass


def get_submissions():
    """Get a list of all submissions filtered based on certian criteria.

    Returns an array of all submissions. It can be filtered based on quizId and/or moduleId and/or userId. For example, a user can request all of their sumissions for any combination of moduleId or quizId. An admin can request all sumbmissions. Admins can filter based on any combination of userId, moduleId, or quizId.

    :param user_id: The user Id of the specific user requesting the submissions.
    :type user_id: str
    :param quiz_id: The quiz Id that a user wants all submissions for
    :type quiz_id: str
    :param module_id: The module Id that a user wants all submissions for
    :type module_id: str

    :rtype: List[Submission]
    """
    pass


def submit_quiz():
    """Take a quiz (user generates a submission)

    When a user finishes a quiz the information they have provided will be stored in a submission object and sent to the backend

    :param body: The submission object for a particular user
    :type body: dict | bytes
    :param quiz_id: The quiz Id for the quiz is the user is submitting
    :type quiz_id: str

    :rtype: None
    """
    pass
