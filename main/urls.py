from django.conf.urls import patterns, include, url

from . import views


prefix = "main_"

urlpatterns = patterns('',
    url(r'^$', views.HomeTemplateView.as_view(), name=prefix + "home"),
)
