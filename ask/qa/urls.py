from django.urls import path, re_path
from django.contrib import admin

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^popular/.*', views.popular, name='popular'),
    re_path(r'^ask/.*', views.test, name='ask'),
    re_path(r'^answer/.*', views.test, name='answer'),
    re_path(r'^signup/.*', views.test, name='signup'),
    re_path(r'^login/.*$', views.test, name='login'),
    re_path(r'^logout/.*', views.test, name='logout'),
    re_path(r'^new/.*$', views.test),
    re_path(r'question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
    path('test/', views.test)
]
