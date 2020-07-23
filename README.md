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
Add export task to django-dbq JOBS list. 
```
JOBS = {
    ...
    'export': {
        'tasks': ['django_dbq_exports.tasks.export_task'],
    },
}
```
Create your export task, for example:
```
def generate_example_report(export_params):
    output_file = 'my_project/tmp/myfile.csv'
    array_length = export_params.get("length", None)
    x = []

    for i in range(array_length if array_length else 99):
        x.append(random.randint(1, 10))

    x = x.sort()
    with open(output_file, 'w') as f:
        f.write(",".join(x))

    return output_file 
```
Setup your exports
```
EXPORTS = {
    "my_export": "my_project.tasks.generate_example_report",
}
```
Setup your url
```
urlpatterns = [
    ...
    url(r'^export/', include("django_dbq_exports.urls")),
]
```
Remember to run your migrations
```
python manage.py migrate
```
