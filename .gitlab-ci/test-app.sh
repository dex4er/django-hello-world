apps="blog"

. .gitlab-ci/helpers/run-linters.sh

cp -f .env.example.sh .env

for db in default django; do
    pipenv run python manage.py migrate --force-color --database $db
done

pipenv run python manage.py check

pipenv run ./manage.py makemigrations --force-color --dry-run --check $apps

pipenv run python manage.py test
