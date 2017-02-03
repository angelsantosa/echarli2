# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import javascript_catalog
from django.views.generic import TemplateView
from django.views import defaults as default_views


# from .views import home, home_files

# 'Packages' should include the names of the app or apps you wish to localize -> eoma
js_info_dict = {
    'domain': 'django',
    'packages': ('perfil','search'),
}

urlpatterns = [
    # DJango apps and cores
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^users/', include("users.urls", namespace="users")),

    url(r'^api/', include('api.urls')),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    # Your stuff: custom urls includes go here
    # Serve catalog of localized strings to be rendered by Javascript
    url(r'^i18n.js$', javascript_catalog, js_info_dict, name='javascript-catalog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permission Denied")}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
    ]

############################# ECHARLI #############################
# Mapeo de URLs de aplicaciones

# URL mappings for profile
urlpatterns += i18n_patterns(
    # Index de l aplicacion
    url(r'^', include('index.urls')),
    #
    url(r'^accounts/', include('allauth.urls')),
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^perfil/', include('perfil.urls')),
    url(r'^search', include('search.urls')),
    url(r'^mentor/', include('mentor.urls')),
    url(r'^publish', include('publish.urls')),
)
