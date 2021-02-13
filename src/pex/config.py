"""
PEX Configuration
"""

import os


class Config:  # pylint: disable=too-few-public-methods
    """
    Configuration Class
    """

    DEBUG = False
    TESTING = False
    VERSION = "0.5.2"
    DESC = "Python EXample Service"
    COMMIT_SHA = os.getenv("COMMIT_SHA", "")
