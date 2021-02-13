import os


class Config(object):
    """
    Configuration Class
    """

    DEBUG = False
    TESTING = False
    VERSION = "0.5.1"
    DESC = "Python EXample Service"
    COMMIT_SHA = os.getenv("COMMIT_SHA", "")
