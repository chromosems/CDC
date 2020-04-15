from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('ministries', views.ministries, name="ministries"),
    path('sermons', views.sermons, name='sermons'),
]
