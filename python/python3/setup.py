#!/usr/bin/env python3
"""
    Purpose:
        setup.py is executed to build the python project and install
        the libraries as a pip project. This will allow for the libs
        to be included in the Dockerfile of projects utilizing these
        libraries.

    Steps:
        - N/A

    function call:
        ./library_tester.py
"""

"""
    Purpose:
        Allows pip install to find required packages and install upon
        installation of this repository.
"""

from setuptools import setup, find_packages

setup(
    name='twosix_py3',
    version='1.0.0',
    python_requires='>3.5',
    description=(
        'TwoSixLabs Python 3.x Resuable Libraries'
    ),
    url='https://github',
    author='',
    author_email='',
    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['python', 'libraries'],
    packages=[
        'execution_helpers',
        'logging_helpers',
    ],
    install_requires=[
        'wrapt==1.10.8',
    ],
    project_urls={},
)
