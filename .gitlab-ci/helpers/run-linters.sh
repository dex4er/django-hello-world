sources=$(echo django_hello_world *.py)

pipenv run black --check .
pipenv run flake8 $sources
pipenv run pylint --rcfile=setup.cfg $sources
pipenv run bandit --ini setup.cfg --recursive --format screen $sources
pipenv run doc8 *.rst
