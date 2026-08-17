from django.urls import path

from . import views

app_name = "clinics"

urlpatterns = [
    path("", views.home, name="home"),
    path("setup/", views.setup, name="setup"),
    path("setup/doctors/", views.add_doctor, name="add_doctor"),
    path("setup/rooms/", views.add_room, name="add_room"),
    path("setup/hours/", views.add_hours, name="add_hours"),
    path("setup/staff/", views.add_staff, name="add_staff"),
]
