.. image:: https://travis-ci.org/dex4er/django-hello-world.svg?branch=develop
   :target: https://travis-ci.org/dex4er/django-hello-world
.. image:: https://gitlab.com/dex4er/django-hello-world/badges/develop/build.svg
   :target: https://gitlab.com/dex4er/django-hello-world/pipelines

Hello, World
============

The template for Django applications.

Django Application
------------------

Pipenv
^^^^^^

.. code:: sh

  pip install pipenv

or

.. code:: sh

  apt install pipenv

or

.. code:: sh

  brew install pipenv

Configuration
^^^^^^^^^^^^^

.. code:: sh

  cp .env.example.sh .env

Then either

.. code:: sh

  set -a; . .env; set +a

or

.. code:: sh

  export READ_ENV=.env

Running from working tree
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

  pip install pipenv
  pipenv install --dev
  pipenv run ./manage.py migrate
  pipenv run ./manage.py runserver

Installing
^^^^^^^^^^

.. code:: sh

  pipenv run ./setup.py bdist_wheel
  virtualenv -ppython3 /opt/django-hello-world
  bash --rcfile /opt/django-hello-world/bin/activate
  pip install dist/django_hello_world-*.whl

Running from package
^^^^^^^^^^^^^^^^^^^^

.. code:: sh

  PATH=/opt/django-hello-world/bin:$PATH
  django-hello-world migrate
  django-hello-world runserver

Database
--------

SQLite
^^^^^^

By default this project uses SQLite databases stored in ``./run/db`` directory.

MySQL
^^^^^

*Debian / Ubuntu*

.. code:: sh

  sudo apt-get install mysql-server mysql-client libmysqlclient-dev

or:

.. code:: sh

  sudo apt-get install mariadb-server mariadb-client libmariadbclient-dev-compat

*Configuration*

.. code:: sh

  cat << END | mysql -v
  CREATE DATABASE hello_world CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  CREATE DATABASE django CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  END
  cat > .my.cnf << END
  [client:hello_world]
  host = localhost
  port = 3306
  user = root
  password =

  [client:django]
  host = localhost
  port = 3306
  user = root
  password =
  END

*Python*

.. code:: sh

  pipenv install mysqlclient

PostgreSQL
^^^^^^^^^^

*Debian / Ubuntu*

.. code:: sh

  sudo apt-get install postgresql libpq-dev
  sudo sed -i '/^# TYPE/alocal all hello md5' /etc/postgresql/*/main/pg_hba.conf
  sudo service postgresql reload
  sudo -i -u postgres createuser --createdb --pwprompt hello
  sudo -i -u postgres createdb --encoding=UTF8 --owner=hello hello
  echo 'localhost:*:hello:hello:hello' >> ~/.pgpass
  echo 'localhost:*:test_hello:hello:hello' >> ~/.pgpass
  chmod 600 ~/.pgpass
  psql -U hello hello -c '\dt'

*Python*

.. code:: sh

  pipenv install psycopg2

systemd
-------

The application can be started using embedded Werkzeug HTTP server that can be
started as a systemd service.

.. code:: sh

  adduser --system --group django-hello-world

``/etc/systemd/system/django-hello-world.service``

.. code:: ini

  [Unit]
  Description=Django Hello World
  After=network.target

  [Service]
  WorkingDirectory=/opt/django-hello-world
  User=django-hello-world
  Group=django-hello-world
  EnvironmentFile=/opt/django-hello-world/.env
  ExecStart=/opt/django-hello-world/bin/django-hello-world runserver --noreload --insecure --threaded --no-color 0.0.0.0:8000
  KillMode=process
  Restart=on-failure

  [Install]
  WantedBy=multi-user.target

Then

.. code:: sh

  systemctl enable django-hello-world.service
  systemctl start django-hello-world.service
  journalctl -f -u django-hello-world.service

Project management
------------------

Repository
^^^^^^^^^^

This repository uses "relaxed" git-flow layout: main leading branch is
``develop`` and the latest stable code is ``master``. The feature and bugfix
branches are merged into ``develop``. Changes from `develop` and `master` are
fast-forwarded.

Versioning
^^^^^^^^^^

This project does not use semantic versioning (it makes sense for libraries).
Version number schema is: ``MAJOR.YYYYMMDD.REL``, where ``MAJOR`` is a real
project version and ``REL`` is a number for a release in the same day.

Version number is stored in a ``django_hello_world/__init__.py`` file (main
project module) and provides ``VERSION`` and ``__version__`` symbols, ie.:

.. code:: python

  VERSION = (0, 20190516, 1)
  __version__ = '.'.join(map(str, VERSION))

Pipelines
^^^^^^^^^

This project provides a configuration for GitLab pipelines that test a project,
build artifacts and tag the latest stable working version.

Pipelines run only for branches (no tags):

* In feature and bugfix branches run tests
* In `develop` branch build, export and test artifacts
* In `master` branch merge and tag arfifacts repo and tag main app repo

Main App repository
^^^^^^^^^^^^^^^^^^^

GitLab pipelines use read-write access to main and artifacts repository using
private SSH deployment key stored in ``SSH_PRIVATE_KEY`` variable.

This repository has changed the default branch to ``develop`` and enabled SSH
deployment key with read-write access.

Artifacts repository
^^^^^^^^^^^^^^^^^^^^

Artifacts are stored in separate Git repository with git-lfs support.

Artifacts repository uses the same layout as a main app repository
(``develop``, ``master``, tags).

Initialization for artifacts repository was:

.. code:: sh

  git init
  git remote add origin $GIT_REPO_PACKAGES_URL
  git checkout -b develop
  git lfs install
  git lfs track "*.gz"
  git lfs track "*.whl"
  git lfs track "*.zip"
  git add .gitattributes
  git commit -m git-lfs .
  git push origin develop

Then the default branch was changed to ``develop``.

This repository has disabled CI pipelines and enabled SSH deployment key with
read-write access.

Offline installation
^^^^^^^^^^^^^^^^^^^^

Artifacts repository allows to install all packages in offline mode.

.. code:: sh

  git clone $GIT_REPO_PACKAGES_URL .packages
  virtualenv -ppython3 /opt/django-hello-world
  bash --rcfile /opt/django-hello-world/bin/activate
  pip install --no-index --find-links .packages --upgrade --requirement dist-requirements.txt

Testing
^^^^^^^

Testing pipieline is started after each push to any branch.

It is possible to run GitLab testing pipeline without GitLab runner using
``docker-compose``.

.. code:: sh

  cd .gitlab-ci
  docker-compose up --abort-on-container-exit --exit-code-from test --force-recreate

Release
^^^^^^^

Release pipeline is started after fast-forward from ``develop`` to ``master``.
This pipeline do fast-forward in artifacts repository and make a new tag based
on a current package version.
