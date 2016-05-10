# app/urls.py

from django.conf.urls import url

from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^test/$', views.test, name='test'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^profile2/$', views.profile2, name='profile2'),
	url(r'^profile3/$', views.profile3, name='profile3')
]