app_package="django_hello_world"
app_script="django-hello-world"

virtualenv --python=python3 --no-download .venv2

. .venv2/bin/activate

cd .packages
    pip install --no-index --find-links $(pwd) -r packages.txt -r dist-packages.txt
cd -

cp -f .env.example.sh .env

for db in default django; do
    READ_ENV=.env $app_script migrate --force-color --database $db
done

READ_ENV=.env $app_script check
