# -*- coding: utf-8 -*-

"""Main module."""

import os
import sys

import invoke
import click


def quote_line(input_line):
    """
    Wraps ``input_line`` with double quotes.

    Useful for paths with spaces.

    :param input_string: string (if not a string, ``str(input_line)`` applied)
    :returns: string
    """
    return '"' + str(input_line) + '"'


def ensure_system_call(raw_cmd):
    """
    System call wrapper that stops the execution if the return code is not 0.

    :param raw_cmd: list of command arguments
    :returns: invoke object
    :raises: program termination
    """
    try:
        return system_call(raw_cmd)
    except SystemCallUnexpectedExitException as err:
        error_exit(err)


def system_call(raw_cmd):
    """
    System call wrapper.

    :requires: invoke
    :param raw_cmd: list of command arguments
    :returns: invoke object
    :raises SystemCallUnexpectedExitException: raises an exception
    """
    # TODO: check if scalar is passed instead of list or tuple
    cmd = ' '.join(raw_cmd)
    try:
        return invoke.run(cmd)
    except invoke.exceptions.UnexpectedExit as err:
        raise SystemCallUnexpectedExitException(
            'Failed call: "{0}":\t{1}'.format(cmd, err)
        )


def error_exit(msg, exit_code=1):
    """
    Program termination wrapper.

    :requires: click
    :param msg: string message to display
    :param exit_code: default value is 1
    :returns: None
    :raises: program termination
    """
    click.secho('[ERROR] {}'.format(msg), bg='red')
    sys.exit(exit_code)


class SystemCallUnexpectedExitException(Exception):
    pass


def ensure_file_exists(file_path):
    """
    Check that ``file_path`` exists and this is file.

    :param file_path: path string
    :returns: None
    :raises: program termination
    """
    if not os.path.exists(file_path):
        error_exit('File "{}" does not exist'.format(file_path))

    if not os.path.isfile(file_path):
        error_exit('Path "{}" is not a file'.format(file_path))


def ensure_dir_exists(dir_path):
    """
    Check that ``dir_path`` is a dir and exists (creates otherwise).

    :param dir_path: path string
    :returns: None
    :raises: program termination
    """
    try:
        os.makedirs(dir_path, exist_ok=True)
    except Exception as err:
        error_exit('Cannot create directory "{}":\n{}'.format(dir_path, err))
