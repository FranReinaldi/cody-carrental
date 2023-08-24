from django.contrib import admin
from django.urls import path, include

from applications.core.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/',include('applications.cars.urls')),
    path('users/', include('applications.users.urls')),
    path('', welcome, name='welcome'),
]
