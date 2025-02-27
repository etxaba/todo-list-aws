#!/bin/bash

source todo-list-aws/bin/activate
set -x
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
echo "PYTHONPATH: $PYTHONPATH"
export DYNAMODB_TABLE=todoUnitTestsTable
export ENDPOINT_OVERRIDE=
python test/unit/TestToDo.py
pip show coverage
coverage run --include=src/todoList.py test/unit/TestToDo.py
coverage report
coverage xml
