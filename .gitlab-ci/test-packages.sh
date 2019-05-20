virtualenv --python=python3 --no-download .venv2

. .venv2/bin/activate

cd .packages
    pip install --no-index --find-links $(pwd) -r packages.txt
cd -

cp -f .env.example.sh .env

for db in default django; do
    python manage.py migrate --force-color --database $db
done

python manage.py check
