from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Register
from .forms import RegisterForm

class IndexView(generic.TemplateView):
    template_name = "index/index.html"

class RegisterView(generic.TemplateView):
    template_name = "register/register.html"
    
class RegisteredView(generic.TemplateView):
    template_name = "registered/registered.html"

def submitted(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
    return HttpResponseRedirect(reverse("register:registered"))
    
    