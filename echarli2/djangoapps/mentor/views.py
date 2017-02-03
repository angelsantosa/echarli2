from django.shortcuts import render
from django.views import generic

# Create your views here or die
class MentorSettingsView(generic.TemplateView):
    template_name = 'mentor/settings.html'
