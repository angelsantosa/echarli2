from __future__ import absolute_import, unicode_literals
from django.conf.urls import patterns, url
from . import views

app_name = 'mentor'
urlpatterns = [
	url(r'^settings$', views.MentorSettingsView.as_view(), name='settings'),
]
