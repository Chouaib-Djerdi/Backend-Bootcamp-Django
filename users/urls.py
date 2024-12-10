from django.urls import path
from .views import register_user, login_user, logout_user

app_name = "users"

urlpatterns = [
    path("register/", register_user, name="register-user"),
    path("login/", login_user, name="login-user"),
    path("logout/", logout_user, name="logout-user"),
]
