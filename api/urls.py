from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("articles/", view=views.ArticleAPIView.as_view()),
    path("articles/<int:pk>", view=views.RetrieveArticleAPIView.as_view()),
    path("auth/register/", view=views.RegisterAPIView.as_view()),
    path("auth/confirm/<str:code>", view=views.ConfirmUser.as_view())
]