from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here or die
class IndexView(TemplateView):
    template_name = 'index/main.html'

class PartialGroupView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context
