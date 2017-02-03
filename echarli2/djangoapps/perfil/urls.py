from django.conf.urls import patterns, url
from perfil.views import PerfilView


urlpatterns = [
    url(r'^$', PerfilView.as_view()),
]