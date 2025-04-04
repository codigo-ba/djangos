from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("reservation/", views.reservation, name="reservation"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.signout, name="logout"),
]