from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import User
from .models import Category, Article, Comment
from .forms import ArticleForm
from .utils import find_tags

def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    context = {
        "categories": categories,
        "articles": articles
    }
    return render(request, "index.html", context)


def article_details_view(request, pk):

    article = get_object_or_404(Article, pk=pk)   
    comments = article.comments.filter(parent=None)

    context = {
        "article": article,
        "comments": comments,
    }

    return render(request=request, template_name="details.html", context=context)


@login_required
def article_creation_view(request):
    form = ArticleForm() 
    categories = Category.objects.all() 

    if request.method == "POST": # При получении метода POST
        form = ArticleForm(data=request.POST, files=request.FILES) # передаём в форму данные запроса и файлы, отправленные пользователем
        if form.is_valid():
            tags = find_tags(request.POST.get("tags")) # определяем: какие теги ввел пользователь
            form.save(request.user, *tags) # создание публикации
            return redirect("news:index")

    context = {
        "categories": categories,
        "form": form,
    }
    return render(request=request, template_name="article.html", context=context)


@login_required
def create_comment_view(request, article_pk: int, parent_pk: int|None = None):
    user: User = request.user
    article = get_object_or_404(Article, pk=article_pk)
    comment = request.POST.get("comment")

    parent = None
    if parent_pk is not None:
        parent = get_object_or_404(Comment, pk=parent_pk)

    Comment.objects.create(
        owner=user,
        article=article,
        comment=comment,
        parent=parent
    )

    return redirect(request.META.get("HTTP_REFERER", "/"))