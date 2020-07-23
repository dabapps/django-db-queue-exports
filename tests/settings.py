DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django_dbq_exports",
    "django_dbq",
)

SECRET_KEY = "abcde12345"

JOBS = {
    "export": {"tasks": ["django_dbq_exports.tasks.export_task"],},
}

EXPORTS = {
    "my_export": "tests.tasks.generate_example_report",
    "failing_export": "some.path.doesnt.exist",
}

ROOT_URLCONF = "tests.urls"
USE_TZ = True
