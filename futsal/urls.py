from django.urls import path
from . import views

app_name = 'futsal'
urlpatterns = [
      path('', views.index, name='index'),
      path('detail/', views.detail, name='detail'),
      path('about/', views.about, name='about'),
      path('contact/', views.contact, name='contact'),
]
