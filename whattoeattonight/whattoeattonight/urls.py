from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("recipes/", include("recipes.urls")),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
