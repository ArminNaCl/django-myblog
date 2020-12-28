from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView as Login , LogoutView as Logout

from .forms import UserRegistrationForm 

# Create your views here.
class RegisteritionView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'account/registerition.html'

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class LoginView(Login):
    template_name = 'account/login.html'

class LogoutView(Logout):
    next_page = '/blog/'