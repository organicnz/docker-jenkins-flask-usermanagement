## Overview

This Flask application contains the basic user management functionality (register, login, logout) to demonstrate the use of pytest.

## Motivation

After reading Brian Okken's book (Python Testing with pytest), I was convinced that I should learn about pytest and then figure out how to use it to test Flask applications.

## How to Run

In the top-level directory:

    $ export FLASK_APP=app.py
    $ export FLASK_ENV=development
    $ flask run

## Installation Instructions

Pull down the source code from this GitLab repository:

```sh
git clone git@gitlab.com:patkennedy79/flask_user_management_example.git```

Create a new virtual environment:

```sh
$ cd flask_user_management_example
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

Set the file that contains the Flask application and specify that the development environment should be used:

```sh
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

## Key Python Modules Used

- Flask: micro-framework for web application development
- Jinga2 - templating engine
- SQLAlchemy - ORM (Object Relational Mapper)
- Flask-Bcrypt - password hashing
- Flask-Login - support for user management
- Flask-WTF - simplifies forms

This application is written using Python 3.8.5.

## Testing

```sh
(venv) $ pytest -v
```
