"""Xadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.contrib import admin
import xadmin
from message import views as msg_views
from job import views as job_views
#from django.views.generic import TemplateView
#url(r'^xadmin/', TemplateView.as_view(template_name='XXX.html')),


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^msg/$', msg_views.msg, name='msg'),
    url(r'^dbtojson/$', job_views.dbtojson, name='dbtojson'),
    url(r'^search/$',job_views.search,name='search'),
    url(r'^$', job_views.index, name='index'),
]
