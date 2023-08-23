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
    path("add-user/", views.AddUser, name="add_user"),
    path(
        "user-profile/<int:user_id>/",
        views.CustomersProfile,
        name="user-profile",
    ),
    path(
        "delete_message/<int:msg_id>/",
        views.Delete_CustomerMessage,
        name="delete_message",
    ),
    path(
        "update_user/<int:profile_id>/",
        views.Update_Customer,
        name="update_user",
    ),
    path(
        "delete_user/<int:profile_id>/",
        views.Delete_Customer,
        name="delete_user",
    ),
    path("admins/", views.Admins, name="admins"),
    path(
        "remove_admin/<int:profile_id>/",
        views.Remove_Admin,
        name="remove_admin",
    ),
    path("properties/", views.PropertyList, name="properties"),
    path(
        "update-property/<int:property_id>/",
        views.UpdateProperty,
        name="update-property",
    ),
    path("add-property/", views.AddProperty, name="add-property"),
    path("sell-requests/", views.Sell_Request_List, name="sell_request_list"),
    path(
        "sell-requests/<int:sellrequest_id>/",
        views.Sell_Request_View,
        name="sellrequest_view",
    ),
]


# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
