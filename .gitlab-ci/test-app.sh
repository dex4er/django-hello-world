sources=$(echo django_hello_world django_hello_world_blog *.py)
pipenv run flake8 $sources
pipenv run pylint --rcfile=setup.cfg $sources
pipenv run bandit --ini setup.cfg --recursive --format screen $sources
pipenv run doc8 *.rst

cp -f .env.example.sh .env

export READ_ENV='no'

pipenv run python manage.py test

for db in default django; do
    pipenv run python manage.py migrate --force-color --database $db
done

pipenv run python manage.py makemigrations --force-color --dry-run --check django_hello_world_blog
pipenv run python manage.py loaddata category note
