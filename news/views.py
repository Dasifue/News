from django.shortcuts import render, get_object_or_404

from .models import Category, Article

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

    context = {
        "article": article
    }

    return render(request=request, template_name="details.html", context=context)