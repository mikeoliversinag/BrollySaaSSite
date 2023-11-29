
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("brolly/", include("brolly.urls")),
    path("admin/", admin.site.urls),
]

