from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.Indexpage, name="index"),
    path("home/", views.Homepage, name="home"),
    path("login/", views.Loginpage, name="login"),
    path("register/", views.RegisterPage, name="register"),
    path("logout/", views.LogoutPage, name="logout"),
    path("profile/", views.ProfilePage, name="profile"),
    path("change-password/", views.ChangePassword, name="change-password"),
]


# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)