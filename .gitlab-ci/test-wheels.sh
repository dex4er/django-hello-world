app_script="django-hello-world"

mkdir -p .venv-wheels
rm -rf .venv-wheels/* .venv-wheels/.??*

virtualenv --python=pypy3 --no-download .venv-wheels

. .venv-wheels/bin/activate

cd .wheels
    pip install --no-index --find-links $(pwd) -r packages.txt -r dist-packages.txt
cd -

cp -f .env.example.sh .env

export READ_ENV=.env

for db in default django; do
    $app_script migrate --force-color --database $db
done

$app_script check
