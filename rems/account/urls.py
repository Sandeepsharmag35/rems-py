from django.urls import path
from . import views

urlpatterns = [
    path("", views.Indexpage, name="index"),
    path("home/", views.Homepage, name="home"),
    path("login/", views.Loginpage, name="login"),
    path("register/", views.RegisterPage, name="register"),
    path("logout/", views.LogoutPage, name="logout"),
    path("profile/", views.ProfilePage, name="profile"),
]
