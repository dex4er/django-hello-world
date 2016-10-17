Hello, World
============

The template for Django applications.

Django Application
------------------

Environment
^^^^^^^^^^^

.. code:: sh

  virtualenv .virtualenv
  . .virtualenv/bin/activate
  pip install -U pip setuptools
  pip install -r requirements.txt

Configuration
^^^^^^^^^^^^^

.. code:: sh

  for f in project/*.dev.example; do cp $f project/`basename $f .dev.example`; done

Running
^^^^^^^

.. code:: sh

  ./manage.py migrate
  ./manage.py runserver

PostgreSQL
----------

Debian / Ubuntu
^^^^^^^^^^^^^^^

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

Environment
^^^^^^^^^^^

.. code:: sh

  pip install -r requirements/db.txt

Configuration
^^^^^^^^^^^^^

.. code:: sh

  cp -f project/settings_db.py.prd.example project/settings_db.py

Cloning of database
^^^^^^^^^^^^^^^^^^^

.. code:: sh

  ssh source-server pg_dump -Fc hello | pg_restore -c -U hello | psql -U hello hello

Variants
--------

The template provides different variants as separate branch:

master
  Basic template

blog
  Simple application with model, view and admin

blog_suite
  Django Suit admin interface

blog_rest
  Additional REST service

blog_search
  Full text search with Haystack + Whoosh

blog_reports
  QuerySet with Django Admin view
