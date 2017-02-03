from __future__ import absolute_import, unicode_literals
from django.conf.urls import patterns, url, include
from . import views

partial_patterns = [
    url(
        r'^home/home.html$',
        views.PartialGroupView.as_view(template_name='app/home/home.html'),
        name='home'
    ),
    url(
        r'^layouts/error/error.html$',
        views.PartialGroupView.as_view(template_name='app/layouts/error/error.html'),
        name='error'
    ),
    url(
        r'^layouts/error/accessdenied.html$',
        views.PartialGroupView.as_view(template_name='app/layouts/error/accessdenied.html'),
        name='accessdenied'
    ),
    url(
        r'^layouts/navbar/navbar.html$',
        views.PartialGroupView.as_view(template_name='app/layouts/navbar/navbar.html'),
        name='navbar'
    ),
    url(
        r'^components/login/login.html$',
        views.PartialGroupView.as_view(template_name='app/components/login/login.html'),
        name='login'
    ),
    # ... more partials ...,
]

urlpatterns = [
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='index'
    ),
    url(r'^app/', include(partial_patterns, namespace='partials')),
]
