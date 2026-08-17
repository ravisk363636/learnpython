from django.urls import path

from . import views

app_name = "appointments"

urlpatterns = [
    path("appointments/", views.book, name="book"),
    path("appointments/<int:appointment_id>/check-in/", views.check_in, name="check_in"),
    path("appointments/<int:appointment_id>/cancel/", views.cancel_appointment, name="cancel"),
]
