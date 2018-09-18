#!/usr/bin/env python3
"""
    Purpose:
        Library for Logging in Docker. This will utilize the logging
        library to python stout to be captured by the docker log
        and generate an optional log within the container
"""

# Python Library Imports
import logging
import sys


def get_docker_logging(level=logging.INFO):
    """
    Purpose:
        Get Docker-Specific Logger. This will log all events to
        stdout instead of a log-file so that 'docker logs' will
        pick up all events.
    Args:
        level (log level from logging):

    Examples:
        >>> from docker_logging import get_logging
        >>> logging = get_logging()
    """

    logging.basicConfig(
        stream=sys.stdout,
        level=level,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S'
    )

    return logging
