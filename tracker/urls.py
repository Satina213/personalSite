from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("log", views.view_logs, name="log"),
]