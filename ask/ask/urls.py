"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from qa.views import test


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', test),
    url(r'^popular/.*', test, name='popular'),
    url(r'^ask/.*', test, name='ask'),
    url(r'^answer/.*', test, name='answer'),
    url(r'^signup/.', test, name='signup'),
    url(r'^login/.*$', test, name='login'),
    url(r'^logout/.*', test, name='logout'),
    url(r'^new/.*$', test),
    url(r'question/(?P<question_id>[0-9]+)/$', test, name='question'),
]
