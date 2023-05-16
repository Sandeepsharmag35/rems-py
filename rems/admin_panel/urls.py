from django.urls import path
from . import views

urlpatterns = [
    path("admin/", views.adminLogin, name="admin_login"),
    path("admin-logout/", views.adminLogout, name="admin_logout"),
    path("dashboard/", views.AdminDashboard, name="admin_dashboard"),
    path("messages/", views.customerMessage, name="messages"),
    path("customers/", views.Customers, name="customers"),
]
