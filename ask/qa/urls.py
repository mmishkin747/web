from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'test'),
    url(r'^popular/.*', 'test', name='popular'),
    url(r'^ask/.*', 'test', name='ask'),
    url(r'^answer/.*', 'test', name='answer'),
    url(r'^signup/.', 'test', name='signup'),
    url(r'^login/.*$', views.test, name='login'),
    url(r'^logout/.*', 'test', name='logout'),
    url(r'^new/.*$', views.test),
    url(r'question/(?P<question_id>[0-9]+)/$', 'test', name='question'),
]
