"""Validate cookiecutter variables before the project is generated."""

import re
import sys

PACKAGE_NAME = '{{ cookiecutter.package_name }}'

# PEP 508 project name, restricted to lowercase for a predictable directory name.
NAME_PATTERN = r'^[a-z0-9]([a-z0-9._-]*[a-z0-9])?$'

if not re.match(NAME_PATTERN, PACKAGE_NAME):
    print(
        f'ERROR: package_name "{PACKAGE_NAME}" is invalid. '
        'Use lowercase letters, digits, ".", "_" or "-", '
        'starting and ending with a letter or digit.'
    )
    sys.exit(1)

if PACKAGE_NAME == 'config':
    print('ERROR: package_name must not be "config" (reserved for the Django settings package).')
    sys.exit(1)
