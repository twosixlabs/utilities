"""
    Purpose:
        Library for Logging in Docker. This will utilize the logging
        library to python stout to be captured by the docker log
        and generate an optional log within the container
"""

# Python Library Imports
import logging
import sys


def get_docker_logging(
    log_level=logging.INFO,
    log_msg_fmt='%(asctime)s %(levelname)s %(message)s',
    log_date_fmt='%a, %d %b %Y %H:%M:%S'
):
    """
    Purpose:
        Get Docker-Specific Logger. This will log all events to
        stdout instead of a log-file so that 'docker logs' will
        pick up all events.
    Args:
        level (Logging Level Enum): Level of logs to show (DEBUG, INFO, ERROR)
        log_msg_fmt (String): Message format. Sets standard for all logs
        log_date_fmt (String): Data format to prefix log (used if asctime)
            is in the log_msg_fmt variable
    Examples:
        >>> from docker_logging import get_logging
        >>> logging = get_logging(level=logging.DEBUG)
    """

    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format=log_msg_fmt,
        datefmt=log_date_fmt
    )

    return logging
