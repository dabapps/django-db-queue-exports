# Django PyPI Template

**An extension to django-db-queue for monitoring long running job statuses.**

[![Build Status](https://travis-ci.com/dabapps/django-pypi-template.svg?token=YbH3f6uroz5f5q8RxDdW&branch=master)](https://travis-ci.com/dabapps/django-db-queue-exports)

## Overview

An extension to django-db-queue for monitoring long running job statuses.


## Getting started
# Installation
Install from PIP
```pip install django-db-queue-exports```
Add django_dbq_exports to your installed apps
```
INSTALLED_APPS = (
    ...
    'django_dbq_exports',
)
```
Add export task to django-dbq JOBS
```
JOBS = {
    ...
    'export': {
        'tasks': ['django-dbq-exports.tasks.export_task'],
    },
}
```
Describe your export
```
BaseExport derivitave goes here
```
Setup your export
```
EXPORTS = {
    'my_export': {
        'class': ['project.common.exports.my_export'],
    },
}
```

The official python documentation has an excellent tutorial on [how to package python projects](packaging.python.org/tutorials/packaging-projects). This template handles all the steps outlined in this tutorial for you.

Template includes:

1. A `setup.py` that makes your life easy.
2. A simple layout that lets you easily run the package's tests using the `runtests` script.
3. A `build` script similar to the DabApps standard `build` script.
4. A script to `publish` your package on PyPI.

_When using this template and things seem to be out of date, please open a PR against this repo to make life of the next developer working with this template easier._

## Creating a new repo

This repo is a _template repository_, so you can generate a repository with the same directory structure and files without copying the commit history. See [how to create a repository from a template.](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)

### Creating your package

- Update the folder name of `/package_name` and go nuts inside this folder. This is where your actual package will live and you can add `Views`, `Models` or whatever is needed for your package.

- Make sure to add any dependencies that your package relies on to `requirements.txt` in the root of your repo.

- Edit `setup.py` and update the settings at the top of the file by replacing everything inside `<>`. _Note: The `<description>` is a short, one-sentence summary of the package. The long description is setup to be what's in the `README`._

- Run the `build` script to install required packages.

### Writing tests for your package

To write tests for you package, treat the `/tests` folder as the Django environment you want to install the package in.

- Edit `settings.py` and update the `package_name` in `INSTALLED_APPS`.

- Add any test specific requirements to `requirements.txt` inside the `/tests` folder.

- Create a `view.py`, `model.py` or whatever a project would need to test your package.

- Write your tests inside `tests.py`.

- Make sure to uncomment `run_tests_with_coverage` in the `runtests` script. (Coverage blows up when there is no code to cover, so we have to leave it commented out in this template.)

- If your package contains any migrations, make sure to uncomment `run_check_migrations` in the `runtestst` script.

- Update the `package_name` in the `runtests` script to run the tests.

## Packaging

For instructions on how to install the package locally and publish it on PyPI, see the [DabApps Docs](https://docs.dabapps.com/backend/publishing-python-package/)
