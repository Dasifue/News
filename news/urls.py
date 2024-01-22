from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path('', views.index, name='index'), #home page
    path('article/<int:pk>', views.article_details_view, name="details"),
    path('article/create/', views.article_creation_view, name="article_creation"),
    path('article/update/<int:pk>', views.article_update_view, name="article_update"),
    path('article/delete/<int:pk>', views.delete_article_view, name="delete_article"),

    path('comment/create/<int:article_pk>', views.create_comment_view, name="comment_create"),
    path('comment/create/<int:article_pk>/parent/<int:parent_pk>', views.create_comment_view, name="comment_answer"),
    path('comment/delete/<int:pk>', views.delete_comment_view, name="comment_delete")
]