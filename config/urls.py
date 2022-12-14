from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.member.urls")),
    path("api/", include("apps.post.urls")),
]