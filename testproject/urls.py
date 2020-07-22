from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', include('testprojectdjango_db_queue_exports.urls'))
]
