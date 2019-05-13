#!/bin/sh

set -e
set -x

pip install pipenv
if [ "$TEST_LINT" = yes ]; then
    pipenv install --dev
else
    pipenv install
fi
