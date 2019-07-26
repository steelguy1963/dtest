from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.invest_list, name='invest_list'),
    url(r'^new/$', views.invest_new, name='invest_new'), 
    url(r'^column/$', views.invest_new_column, name='invest_new_column'), 
]