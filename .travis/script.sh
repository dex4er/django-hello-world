#!/bin/sh

set -e
set -x

sources=$(echo django_hello_world django_hello_world_blog *.py)

if [ "$TEST_LINT" = yes ]; then
    pipenv run flake8 $sources
    pipenv run pylint --rcfile=setup.cfg $sources
    pipenv run bandit --ini setup.cfg --recursive --format screen $sources
    pipenv run doc8 *.rst
fi

cp -f .env.example.sh .env

export READ_ENV='no'

pipenv run python manage.py test

for db in default django; do
    pipenv run python manage.py migrate --force-color --database $db
done

pipenv run python manage.py makemigrations --force-color --dry-run --check django_hello_world_blog
pipenv run python manage.py loaddata category note
