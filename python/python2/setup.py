"""
    Purpose:
        setup.py is executed to build the python 2.x project and install
        the libraries as a pip project. This will allow for the libs
        to be included in the Dockerfile of projects utilizing these
        libraries.
"""

from setuptools import setup, find_packages

setup(
    name='twosix_py2',
    version='1.0.0',
    python_requires='<3.0.0',
    description=(
        'TwoSixLabs Python 2.x Resuable Libraries'
    ),
    url='https://github.com/twosixlabs/utilities/python/python2',
    author="Two Six Labs",
    author_email="magicwand@twosixlabs.com",
    classifiers=[
        'Programming Language :: Python :: 2.x',
    ],
    keywords=['python', 'libraries'],
    packages=[
        'execution_helpers',
        'logging_helpers',
    ],
    install_requires=[
        'wrapt>=1.10.8',
    ],
    project_urls={},
)
