from django.urls import path

from . import views

app_name = "queues"

urlpatterns = [
    path("queue/issue/", views.issue, name="issue"),
    path("queue/call/<int:doctor_id>/", views.call_next_view, name="call_next"),
    path("queue/token/<int:token_id>/", views.token_action, name="token_action"),
    path("queue/doctor/", views.doctor_queue, name="doctor_queue"),
    path("queue/doctor/<int:doctor_id>/pause/", views.pause_queue, name="pause"),
    path("board/<slug:slug>/", views.tv_board, name="tv_board"),
    path("p/<str:signed>/json/", views.patient_status_json, name="patient_status_json"),
    path("p/<str:signed>/", views.patient_status, name="patient_status"),
]
