from django.urls import path
from . import views

urlpatterns = [
    path("admin/", views.adminLogin, name="admin_login"),
    path("admin-logout/", views.adminLogout, name="admin_logout"),
    path("dashboard/", views.AdminDashboard, name="admin_dashboard"),
    path("messages/", views.customerMessage, name="messages"),
    path("customers/", views.Customers, name="customers"),
    path(
        "update_customer/<int:profile_id>/",
        views.Update_Customer,
        name="update_customer",
    ),
    path(
        "delete_customer/<int:profile_id>/",
        views.Delete_Customer,
        name="delete_customer",
    ),
    path("admins/", views.Admins, name="admins"),
    path("properties/", views.PropertyList, name="properties"),
    path("add-property/", views.AddProperty, name="add-property"),
]
