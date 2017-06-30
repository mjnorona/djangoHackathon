from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login', views.login),
    url(r'^home$', views.home),
    url(r'^submit/(?P<id>\d+)$', views.submit, name = "submit"),
    url(r'^solutions/(?P<id>\d+)$', views.solutions, name = "solutions"),
    url(r'^like/(?P<id>\d+)$', views.like, name = 'like'),
    url(r'^logout$', views.logout)
]