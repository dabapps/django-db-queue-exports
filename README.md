# django-db-queue-exports

**An extension to [django-db-queue](https://github.com/dabapps/django-db-queue) for monitoring long running task statuses.
The aim of this extension is to simplify the execution of long running tasks, and allow for polling of tasks statuses during execution.**

[![Build Status](https://travis-ci.org/dabapps/django-db-queue-exports.svg)](https://travis-ci.org/dabapps/django-db-queue-exports)

Supported and tested against:
- Django 2.2
- django-db-queue 1.3.0
- Python 3.6, 3.7 and 3.8

## Getting started
### Installation
Install from PIP
```
pip install django-db-queue-exports
```
Add `django_dbq_exports` to your installed apps
```
INSTALLED_APPS = (
    ...
    'django_dbq_exports',
)
```
Add `django_dbq_exports.tasks.export_task` to django-dbq JOBS list in settings.py
```
JOBS = {
    ...
    'export': {
        'tasks': ['django_dbq_exports.tasks.export_task'],
    },
}
```
Configure the url, something like this:
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
### Describing your task
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
Configure your task in settings.py
```
EXPORTS = {
    "my_export": "my_project.tasks.generate_example_report",
}
```

### Running the task
Simply `POST` to the pre-configured endpoint with the following json
```
{
    "export_type" : "my_export"
} 
```
With optional parameters to be received by your previously created export task
```
{
    "export_type" : "my_export",
    "export_params" : {
        "length": 256
    }
}
```
### Querying the task status
Simple `GET` the same endpoint with a url parameter = to the export `id` field returned from the POST request.
Or `GET` the same endpoint with no parameters to return a list of all exports.


## Code of conduct

For guidelines regarding the code of conduct when contributing to this repository please review [https://www.dabapps.com/open-source/code-of-conduct/](https://www.dabapps.com/open-source/code-of-conduct/)