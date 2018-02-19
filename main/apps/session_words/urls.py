from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_word$', views.process),
    url(r'^clear$', views.clear)
]