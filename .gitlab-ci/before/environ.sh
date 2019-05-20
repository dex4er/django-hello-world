set -e
set -o pipefail
set -x

export LANG="C.UTF-8"
export DEBIAN_FRONTEND="noninteractive"
export LANG="C.UTF-8"
export XDG_CACHE_HOME="${CI_PROJECT_DIR:-$PWD}/.cache"
export PIP_CACHE_DIR="$XDG_CACHE_HOME/pip"
export PIPENV_CACHE_DIR="$XDG_CACHE_HOME/pipenv"
export PIPENV_DONT_LOAD_ENV="yes"
export PIPENV_VENV_IN_PROJECT="yes"
export READ_ENV=".env"
