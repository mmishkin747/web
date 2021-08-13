from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^popular/.*', views.popular, name='popular'),
    url(r'^ask/.*', views.ask, name='ask'),
    url(r'^answer/.*', views.answer, name='answer'),
    url(r'^signup/.*', views.test, name='signup'),
    url(r'^login/.*$', views.test, name='login'),
    url(r'^logout/.*', views.test, name='logout'),
    url(r'^new/.*$', views.test),
    url(r'question/(?P<question_id>[0-9]+)/$',
        views.question, name='question'),
    url('test/', views.test)
]
