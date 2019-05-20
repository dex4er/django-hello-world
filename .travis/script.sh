#!/bin/sh

set -e
set -x

apps="django_hello_world_blog"
sources=$(echo $apps django_hello_world *.py)

if [ "$TEST_LINT" = yes ]; then
    pipenv run flake8 $sources
    pipenv run pylint --rcfile=setup.cfg $sources
    pipenv run bandit --ini setup.cfg --recursive --format screen $sources
    pipenv run doc8 *.rst
fi

cp -f .env.example.sh .env

export READ_ENV=".env"
export SITE_DIR=$TRAVIS_BUILD_DIR

pipenv run python manage.py test

for db in default django; do
    pipenv run python manage.py migrate --force-color --database $db
done

pipenv run python manage.py makemigrations --force-color --dry-run --check $apps
pipenv run python manage.py loaddata category note
