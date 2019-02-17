from django.contrib import admin
from django.urls import path, include
from futsal import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('futsal/', include('futsal.urls')),
]
