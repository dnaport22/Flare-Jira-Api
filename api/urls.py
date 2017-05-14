from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.request_handler, name='index'),
]