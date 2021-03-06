PJ job
======

PJ job

**Test site url:** http://127.0.0.1:8895/

**Test admin panel:** http://127.0.0.1:8895/admin/

- Login: `admin`
- Password: `adminadmin`

-------
Agreement
=========

- The `(.env)$` identifier of command line is indicates that there must be active virtual environment.

- In this manual path to the project, for example: `/full/path/to/the/pjjob/` - it will be designated as `$BASE_DIR`.


Attention
=========

- Python support: `3.5.1`

-------

Quick start guide
=================

Clone
-----


    $ git clone git@github.com:bilabon/pjjob.git
    $ cd pjjob


Install virtualenv
------------------


    $ pyvenv .env
    $ source .env/bin/activate
    (.env)$


Install packages
----------------


    (.env)$ pip install -r requirements.txt


Run the project's tests
----------------


    (.env)$ make test


Run the project
----------------


    (.env)$ make migrate
    (.env)$ make fixtures
    (.env)$ make collectstatic
    (.env)$ make run


BOWER USAGE
----------------


    (.env)$ npm install -g bower
    (.env)$ ./manage.py bower install
    (.env)$ make collectstatic


Create MySQL database
-----


    $ sudo mysql -uroot -p

    drop database if exists `pjjob`;
    CREATE DATABASE `pjjob` CHARACTER SET utf8 COLLATE utf8_general_ci;
    GRANT ALL ON `pjjob`.* TO `<USER>`@localhost IDENTIFIED BY '<PASSWORD>';
    FLUSH PRIVILEGES;


if you want to use MySQL database, just create file: `touch basic/local_settings.py` with content:


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pjjob',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'PORT': '',
            'OPTIONS': {'charset': 'utf8',
                        'init_command': 'SET storage_engine=INNODB, \
                        SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED'},
            'TEST': {
                'COLLATION': 'utf8_general_ci',
                'CHARSET': 'utf8',
            },
        }
    }
