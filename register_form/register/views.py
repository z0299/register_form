from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Register

class IndexView(generic.TemplateView):
    template_name = "register/register.html"

def register(request):
    register_form = get_object_or_404(Register)
    