from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^courses/add$', views.new),
    url(r'^courses/destroy/(?P<course_id>\d+)$', views.areyousure),
    url(r'^courses/(?P<course_id>\d+)/destroy$', views.destroy)
]