pipenv lock --requirements > requirements.txt
echo -r requirements.txt > dev-requirements.txt
pipenv lock --dev --requirements >> dev-requirements.txt
pipenv run pip install -r dev-requirements.txt
