import os
import re
import yaml

from distutils.spawn import find_executable

from popper.cli import log


def sanitized_name(name, wid=''):
    """Clean a step name and change it to proper format. It replaces all the
    unwanted characters with `_`.

    Args:
      name(str): The crud step name.
      wid(str): It  is a workflow ID produced by a utils.get_id().

    Returns:
      str: The sanitize step name.
    """
    return f"popper_{re.sub('[^a-zA-Z0-9_.-]', '_', name)}_{wid}"


def of_type(param, valid_types):
    """Function to check the type of a parameter.

    It tries to match the type of the parameter with the
    types passed through `valid_types` list.

    Args:
      param: A value of any type.
      valid_types(list): A list of acceptable types.

    Returns:
      bool: True/False, depending upon whether the type of
      the passed param matches with any of the valid types.
    """
    for t in valid_types:
        if t == 'str':
            if isinstance(param, str):
                return True

        if t == 'dict':
            if isinstance(param, dict):
                return True

        if t == 'los':
            if isinstance(param, list):
                res = list(map(lambda a: isinstance(a, str), param))
                return False not in res

    return False


def assert_executable_exists(command):
    """Check if the given command can be invoked; fails if not."""
    if not find_executable(command):
        log.fail(f"Could not find '{command}'.")


def prettystr(a):
    """improve how dictionaries get printed"""
    if isinstance(a, os._Environ):
        a = dict(a)
    if isinstance(a, dict):
        return f'{yaml.dump(a, default_flow_style=False)}'


def key_value_to_flag(k, v, equals_symbol=False):
    is_bool = isinstance(v, bool)

    if is_bool and not v and not equals_symbol:
        return ''

    flag = '-' if len(k) == 1 else '--'

    if equals_symbol:
        flag += f'{k}={str(v).lower() if is_bool else v}'
    else:
        if isinstance(v, bool):
            flag += f'{k}'
        else:
            flag += f'{k} {v}'
    return flag
