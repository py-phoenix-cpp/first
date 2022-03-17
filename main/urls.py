from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', Index, name='index'),
    path('', include('mainapp.urls')),
]
