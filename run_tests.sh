#!/bin/bash

set -e

./.venv/Scripts/python.exe -m pytest

echo "All tests passed!"
exit 0