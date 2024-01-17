from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", view=views.register_view, name="register"),
    path("login/", view=views.login_view, name="login"),
    path("logout/", view=views.logout_view, name="logout"),

    path("password/change/", view=views.change_password_view, name="change_password"),

    path("favorites/", view=views.favorites_view, name="favorites"),
    path("favorites/add/<int:article_pk>", view=views.add_to_favorites_view, name="add_to_favorites"),
    path("favorites/remove/<int:article_pk>", view=views.remove_from_favorites_view, name="remove_from_favorites"),
]