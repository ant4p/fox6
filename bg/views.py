from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ShowPage(TemplateView):
    template_name = 'bg/index.html'

