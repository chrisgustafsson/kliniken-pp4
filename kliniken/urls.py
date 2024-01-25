from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("signup/", views.signup, name="Sign up"),
    path("login/", views.login, name="Log in"),
]
