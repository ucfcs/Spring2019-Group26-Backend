# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "asltutor"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


setup(
    name=NAME,
    version=VERSION,
    author="Richard Sweetman",
    description="ASL Tutor API",
    author_email="",
    url="",
    keywords=["Swagger", "ASL Tutor API"],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['app=app.__main__:main']},
    long_description="""\
    Full API documentation for ASL tutor backend
    """,
    python_requires='>=3.0'
)
