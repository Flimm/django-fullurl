import django
from . import views

if django.VERSION < (3, 2):
    from django.conf.urls import url as re_path
else:
    from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^foobar$', views.example, name='example'),
]
