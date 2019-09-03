cd $(dirname $0)/../..

rm -rf .packages .venv .venv-packages .venv-wheels .wheels

# before_script
. .gitlab-ci/before/environ.sh
. .gitlab-ci/before/apt.sh
. .gitlab-ci/before/python.sh
. .gitlab-ci/before/pypy3.sh
. .gitlab-ci/before/libxml2.sh
. .gitlab-ci/before/pipenv.sh

# make:venv
. .gitlab-ci/make-venv.sh

# test:app
. .gitlab-ci/test-app.sh

# make:packages:develop
. .gitlab-ci/make-packages.sh

# test:packages:develop:
. .gitlab-ci/test-packages.sh

# make:wheels:develop
. .gitlab-ci/make-wheels.sh

# test:wheels:develop:
. .gitlab-ci/test-wheels.sh

exit 0
