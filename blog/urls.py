from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^json/$', views.post_json, name='post_json'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]