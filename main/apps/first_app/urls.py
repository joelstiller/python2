from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.newblog),
    url(r'^\d+$', views.number),
    url(r'^\d+/edit$', views.edit),
    url(r'^\d+/delete$', views.destroy)  ,
]
