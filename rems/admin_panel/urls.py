from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("admin/", views.adminLogin, name="admin_login"),
    path(
        "admin/",
        auth_views.LoginView.as_view(template_name="admin/admin-login.html"),
        name="admin_login",
    ),
    path("admin-logout/", views.adminLogout, name="admin_logout"),
    path("dashboard/", views.AdminDashboard, name="admin_dashboard"),
    path("messages/", views.customerMessage, name="messages"),
    path("users/", views.Customers, name="users"),
    path("customers-profile/", views.CustomersProfile, name="customers-profile"),
    path(
        "delete_message/<int:msg_id>/",
        views.Delete_CustomerMessage,
        name="delete_message",
    ),
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
    path(
        "remove_admin/<int:profile_id>/",
        views.Remove_Admin,
        name="remove_admin",
    ),
    path("properties/", views.PropertyList, name="properties"),
    path("add-property/", views.AddProperty, name="add-property"),
    path("sell-requests/", views.SellRequestView, name="sell-requests"),
]


# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
