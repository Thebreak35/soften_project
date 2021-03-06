from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from register import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.log, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
]
