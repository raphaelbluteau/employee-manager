# employee-manager
A simple employee manager API using Django Rest Framework

[![Build Status](https://travis-ci.org/raphaelbluteau/employee-manager.svg?branch=master)](https://travis-ci.org/raphaelbluteau/employee-manager) [![Coverage Status](https://coveralls.io/repos/github/raphaelbluteau/employee-manager/badge.svg?branch=master)](https://coveralls.io/github/raphaelbluteau/employee-manager?branch=master)

## Requirements

- Python3, pip3 and SQLite3

## Setup

```sh
$ pip3 install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
You need an admin user account. You can create one running this command and following the instructions:
```sh
$ python3 manage.py createsuperuser
```

Now you can run the server:
```sh
$ python3 manage.py runserver
```

You can run the unit tests with this command:
```sh
$ python3 manage.py test
```

The Django admin page will be available at http://localhost:8000/admin and the API endpoint at http://localhost:8000/employee .
