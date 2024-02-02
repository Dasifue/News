from rest_framework import generics

from .serializers import ArticleSerializer

from news.models import Article



class ArticleAPIView(generics.ListCreateAPIView): 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class RetrieveArticleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "pk"
