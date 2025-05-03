from django.urls import path
from.views import UserCreateView,main,UserLohinView

urlpatterns = [
    
    path('sign-up',UserCreateView.as_view(),name='user-singup'),
    path('login',UserLohinView.as_view(),name='user-login'),
    path('',main,name='main')
]
