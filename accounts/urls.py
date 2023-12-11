from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", view=views.register_view, name="register"),
    path("login/", view=views.login_view, name="login"),
    path("logout/", view=views.logout_view, name="logout"),

    path("password/change/", view=views.change_password_view, name="change_password")
]