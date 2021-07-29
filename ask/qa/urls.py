from django.urls import path, re_path
from django.contrib import admin

from .views import test

urlpatterns = [
    re_path(r'^$', test),
    re_path(r'^popular/.*', test, name='popular'),
    re_path(r'^ask/.*', test, name='ask'),
    re_path(r'^answer/.*', test, name='answer'),
    re_path(r'^signup/.', test, name='signup'),
    re_path(r'^login/.*$', test, name='login'),
    re_path(r'^logout/.*', test, name='logout'),
    re_path(r'^new/.*$', test),
    re_path(r'question/(?P<question_id>[0-9]+)/$', test, name='question'),
    path('test/', test)
]
