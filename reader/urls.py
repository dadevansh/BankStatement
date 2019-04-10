from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_json/$', views.api_req, name='create_json'),
    url(r'^register/$', views.register, name='register'),
]