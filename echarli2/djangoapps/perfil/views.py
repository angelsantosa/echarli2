from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _


class PerfilView(TemplateView):
    template_name = 'perfil/settings.html'
