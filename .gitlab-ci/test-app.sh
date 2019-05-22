apps="blog"
sources=$(echo django_hello_world *.py)

pipenv run black --check .
pipenv run flake8 $sources
pipenv run pylint --rcfile=setup.cfg $sources
pipenv run bandit --ini setup.cfg --recursive --format screen $sources
pipenv run doc8 *.rst

cp -f .env.example.sh .env

for db in default django; do
    pipenv run python manage.py migrate --force-color --database $db
done

pipenv run python manage.py check

pipenv run ./manage.py makemigrations --force-color --dry-run --check $apps

pipenv run python manage.py test
