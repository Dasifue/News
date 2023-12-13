from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:pk>', views.article_details_view, name="details"),
    path('article/create/', views.article_creation_view, name="article_creation"),
]