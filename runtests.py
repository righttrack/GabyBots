#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gbots.test_settings")
    os.environ.setdefault("REUSE_DB", "1")

    from django.core.management import execute_from_command_line

    execute_from_command_line(["manage.py", "test"] + sys.argv[1:])
