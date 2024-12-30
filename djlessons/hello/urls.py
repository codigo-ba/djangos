from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("claude", views.claude, name="claude"),
    path("marcus", views.marcus, name="marcus")
]