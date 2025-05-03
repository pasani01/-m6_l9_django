from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class UserCreateView(CreateView):
    model=User
    fields=('username','first_name','last_name','email','password')
    template_name='signup.html'
    success_url=reverse_lazy('student-list')

class UserLohinView(LoginView):
    template_name='login.html'
    authentication_form=AuthenticationForm
    def get_success_url(self):
        return reverse_lazy('student-list')

    
def main(request):
    return render(
        request,
        'base.html'

    )


# Create your views here.
