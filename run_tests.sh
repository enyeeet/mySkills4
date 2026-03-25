#!/bin/bash

set -e

./.venv/Scripts/python.exe -m pytest

PYTEST_EXIT_CODE=$?

# exit 0 if all tests pass, 1 otherwise
if [ $PYTEST_EXIT_CODE -eq 0 ]; then
    exit 0
else
    exit 1
fi