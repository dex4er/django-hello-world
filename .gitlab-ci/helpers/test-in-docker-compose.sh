cd $(dirname $0)/../..

# before_script
. .gitlab-ci/before/environ.sh
. .gitlab-ci/before/apt.sh
. .gitlab-ci/before/python.sh
. .gitlab-ci/before/pipenv.sh

# make:venv
. .gitlab-ci/make-venv.sh

# test:app
. .gitlab-ci/test-app.sh

# make:packages:develop
. .gitlab-ci/make-packages.sh

# test:packages:develop:
. .gitlab-ci/test-packages.sh

exit 0
