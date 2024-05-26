from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("about/", views.aboutpage, name="about"),
    path("agents/", views.agentspage, name="agents"),
    path("blog/", views.blogpage, name="blog"),
    path("blogdetails/", views.blogdetailspage, name="blogdetails"),
    path("buy/", views.buypage, name="buy"),
    path("contact/", views.contactpage, name="contact"),
    path("rent/", views.rentpage, name="rent"),
    path("sell/", views.sellpage, name="sell"),
    path(
        "property-details/<str:model>/<int:pk>/",
        views.propertyDetailsPage.as_view(),
        name="property-details",
    ),
    path("search-result/", views.SearchResultPage, name="search-result"),
]

# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
