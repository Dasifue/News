from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("articles/", view=views.ArticleAPIView.as_view()),
    path("articles/<int:pk>", view=views.RetrieveArticleAPIView.as_view()),
]