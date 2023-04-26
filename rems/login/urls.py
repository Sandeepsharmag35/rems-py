from django.urls import path
from . import views

urlpatterns = [
    path("login", views.Loginpage, name="login"),
    path("register", views.RegisterPage, name="register"),
    path("logout/", views.LogoutPage, name="logout"),
    path("", views.Homepage, name="index"),
]
