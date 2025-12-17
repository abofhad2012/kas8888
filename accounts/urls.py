from django.urls import path
from .views import profile, register, user_login, user_logout, dashboard

app_name = "accounts"

urlpatterns = [
    path("", profile, name="profile"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
]
