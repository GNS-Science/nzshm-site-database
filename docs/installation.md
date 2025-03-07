# Installation

Instructions for installing the repository on your local computer. Note that this is not required for updating and maintaining the database. However, you may find it continent to use the git CLI for your workflow.

If you are using ssh for GitHub authentication (reccomended) follow [these instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

The project requires python version 3.10 or above; these instructions will use python3.10

## Clone the repository

ssh:
```console
$ git clone git@github.com:GNS-Science/nzshm-site-database.git
$ cd nzshm-site-database
```

or if using https:
```console
$ git clone https://github.com/GNS-Science/nzshm-site-database.git
$ cd nzshm-site-database
```

## Setup your virtual environment and install

Python virtual environments are used to keep dependencies of different projects separate from one another to avoid clashes and to make sure you are using the correct version of python. See [the documentation for more information](https://docs.python.org/3/library/venv.html).

You can use a package manager such as [poetry](https://python-poetry.org/) to install the package, but these instructions will use `venv` and `pip`
```console
$ python3.10 -m venv ~/.virtualenv/nzshm-site-database
```

You can then start your virtual environmnet:
```console
$ source ~/.virtualenv/nzshm-site-database/bin/activate
(nzshm-site-database) $ pip install -e .
```

This will install the package and all its dependencies in your virtual environment. The installation will be in editable mode (`-e`) so that any changes you make to the code will be immediately effective.

To leave the virtual environment simply deactivate it.
```console
(nzshm-site-database) $ deactivate
```

## Test the website

You can run a test of the website on your local computer. First you need to build the documentation. In the project directory, start your virtual environment and then
```console
(nzshm-site-database) $ python nzshm_site_database/scripts/build_docs.py
```

Then build the site and run the server:
```console
(nzshm-site-database) $ mkdocs serve
```
