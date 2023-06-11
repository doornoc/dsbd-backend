from django.urls import path, include

from . import views

app_name = "ticket"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.ticket_add, name="add"),
]
