#!/usr/bin/python3

"""
Run the decision task with fake Taskcluster APIs, to catch Python errors before pushing.
"""

import os, sys
from unittest.mock import MagicMock

class TaskclusterRestFailure(Exception):
    status_code = 404

class Index:
    def __init__(self, options):
        pass

    def findTask(self, _):
        raise TaskclusterRestFailure

Queue = stringDate = fromNow = slugId = os.environ = MagicMock()
sys.modules["taskcluster"] = sys.modules[__name__]
sys.dont_write_bytecode = True
exec(open("decision-task.py").read())
