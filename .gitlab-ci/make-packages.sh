find=$(command -v gfind || command -v find)

mkdir -p .packages

rm -f .packages/*
cp -f Pipfile .packages/Pipfile

pipenv lock --requirements > .packages/requirements.txt
pipenv run pip download -r .packages/requirements.txt -d .packages

$find .packages -maxdepth 1 -regextype egrep -regex '.*\.(gz|whl|zip)' -printf "%P\n" | sort > .packages/packages.txt

echo -r requirements.txt > .packages/dev-requirements.txt
pipenv lock --dev --requirements >> .packages/dev-requirements.txt
pipenv run pip download -r .packages/dev-requirements.txt -d .packages

$find .packages -maxdepth 1 -regextype egrep -regex '.*\.(gz|whl|zip)' -printf "%P\n" | sort > .packages/dev-packages.txt

export SOURCE_DATE_EPOCH=315532800

pipenv run python setup.py sdist bdist_wheel

$find dist -maxdepth 1 -name '*.whl' -printf "%P\n" > .packages/dist-packages.txt

cp -f dist/*.whl .packages
