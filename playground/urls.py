from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'playground'
#URL condfiguration
urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout')
]