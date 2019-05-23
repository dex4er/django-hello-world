app_package="django_hello_world"
app_script="django-hello-world"

virtualenv --python=python3 --clear --no-download .venv2

. .venv2/bin/activate

cd .packages
    pip install --no-index --find-links $(pwd) -r packages.txt -r dist-packages.txt
cd -

cp -f .env.example.sh .env

export READ_ENV=.env

for db in default django; do
    $app_script migrate --force-color --database $db
done

$app_script check
