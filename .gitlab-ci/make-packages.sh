find=$(command -v gfind || command -v find)

mkdir -p .packages

rm -f .packages/*
cp -f Pipfile .packages/Pipfile

pipenv lock --requirements | grep -v ^-i > .packages/requirements.txt
pipenv run pip download -r .packages/requirements.txt -d .packages

$find .packages -maxdepth 1 -regextype egrep -regex '.*\.(gz|whl|zip)' -printf "%P\n" | sort > .packages/packages.txt

pipenv lock --dev --requirements | grep -v ^-i > .packages/dev-requirements.txt
pipenv run pip download -r .packages/dev-requirements.txt -d .packages

$find .packages -maxdepth 1 -regextype egrep -regex '.*\.(gz|whl|zip)' -printf "%P\n" | sort > .packages/dev-packages.txt

export SOURCE_DATE_EPOCH=315532800

pipenv run python setup.py sdist bdist_wheel

python3 -c 'import configparser;c=configparser.ConfigParser();c.read("setup.cfg");print(c["metadata"]["name"])' > .packages/dist-requirements.txt
$find dist -maxdepth 1 -name '*.whl' -printf "%P\n" | sort | tail -n1 > .packages/dist-packages.txt

cp -f dist/*.whl .packages
