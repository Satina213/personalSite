from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("william", views.william, name="william"),
    path("david", views.david, name="david"),
    path("jessica", views.jessica, name="jessica"),
    path("bob", views.bob, name="bob"),
    path("<str:name>", views.greet, name="greet"),
]