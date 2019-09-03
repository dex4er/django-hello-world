find=$(command -v gfind || command -v find)

mkdir -p .wheels

rm -f .wheels/*
cp -f Pipfile .wheels/Pipfile

pipenv lock --requirements | grep -v ^-i > .wheels/requirements.txt
pipenv run pip wheel -r .wheels/requirements.txt -w .wheels

$find .wheels -maxdepth 1 -regextype egrep -regex '.*\.whl' -printf "%P\n" | sort > .wheels/wheels.txt

export SOURCE_DATE_EPOCH=315532800

pipenv run python setup.py bdist_wheel

python3 -c 'import configparser;c=configparser.ConfigParser();c.read("setup.cfg");print(c["metadata"]["name"])' > .wheels/dist-requirements.txt
$find dist -maxdepth 1 -name '*.whl' -printf "%P\n" | sort | tail -n1 > .wheels/dist-wheels.txt

cp -f dist/*.whl .wheels
