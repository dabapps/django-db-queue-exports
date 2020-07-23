from django.urls import path, include

urlpatterns = [
    path("export/", include("django_dbq_exports.urls")),
]
