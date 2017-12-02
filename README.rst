Infty
=====

Infty Project

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: GPLv3


Local development without docker
--------------------------------
# Local development on Linux Ubuntu 16.04.

## Install PostgreSQL, and create infty db.
```
sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-9.6

su postgres

psql

create role <your_linux_user> CREATEDB LOGIN;

vim /etc/postgresql/9.6/main/pg_hba.conf

local: trust
host: trust
host: trust

service postgresql restart

su <your_linux_user>

createdb <your_linux_user>

createdb infty
```
## Install dependencies and migrate db.
```
pip install -r requirements/local.txt

python manage.py migrate
```

## Check if all works.
```
py.test
```


Local (Development) installation
--------------------------------
WIP
explain about .env, DOT_ENV_FILE, READ_DOT_ENV_FILE


Setup the node
--------------
NB!: Install ```ansible-galaxy install thefinn93.letsencrypt``` (use at least ansible version 2.4.0.0)

About ANSIBLE_VAULT_PASSWORD_FILE and .vault_password.txt
This is the ansible-vault password file that should be presented and passed (with environment variable, for example)
for decryption ```.env_production.vault``` on the production server.

So the ```.env_production``` should be ENCRYPTED with password that stored in the ```.vault_password.txt``` file.

Next, for example, to setup the node from "staging" inventory, run:

* ansible-playbook -v -i deploy/ansible/inventories/staging deploy/ansible/site.yml --extra-vars="scenario=init"



Deployment
----------
* ANSIBLE_VAULT_PASSWORD_FILE=.vault_password.txt ansible-playbook -v -i deploy/ansible/inventories/staging deploy/ansible/site.yml


Deployment from Travis
----------------------
You should to add public key (travis_rsa.pub, for e.g.) to the node's authorized_keys
The encrypted (ansible-vault) private key (named travis_rsa.vault) should be added to the repo


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd infty
    celery -A infty.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

.. _mailhog: https://github.com/mailhog/MailHog

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``




Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



