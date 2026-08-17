from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("", include("apps.clinics.urls")),
    path("", include("apps.queues.urls")),
    path("", include("apps.appointments.urls")),
]
