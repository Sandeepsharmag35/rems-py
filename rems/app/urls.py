from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.aboutpage, name="about"),
    path("agents/", views.agentspage, name="agents"),
    path("blog/", views.blogpage, name="blog"),
    path("blogdetails/", views.blogdetailspage, name="blogdetails"),
    path("buy/", views.buypage, name="buy"),
    path("contact/", views.contactpage, name="contact"),
    path("property-details/", views.propertyDetailsPage, name="property-details"),
    path("rent/", views.rentpage, name="rent"),
    path("sell/", views.sellpage, name="sell"),
    path("properties/", views.buySaleRentPage, name="buysalerent"),
]
