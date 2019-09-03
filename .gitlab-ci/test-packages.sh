app_script="django-hello-world"

mkdir -p .venv-packages
rm -rf .venv-packages/* .venv-packages/.??*

virtualenv --python=pypy3 --no-download .venv-packages

. .venv-packages/bin/activate

cd .packages
    pip install --no-index --find-links $(pwd) -r dev-packages.txt
cd -

cp -f .env.example.sh .env

pipenv run python setup.py sdist bdist_wheel

export READ_ENV=.env

pipenv run python manage.py check
