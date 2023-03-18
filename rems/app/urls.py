from django.urls import path
from . import views

urlpatterns = [
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('home/', views.homepage, name='home'),


]
