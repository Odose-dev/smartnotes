from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# Create your views here.

class SignupInterfaceView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = reverse_lazy('login') 
    
    
class LogoutInterfaceView(LogoutView):
   # template_name = 'home/logout.html'
    next_page = '/'
    
    
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url='/admin'

 