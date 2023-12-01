from django.shortcuts import render

from .models import Category, Article

def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    context = {
        "categories": categories,
        "articles": articles
    }
    return render(request, "index.html", context)
