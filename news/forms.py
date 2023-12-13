from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("name", "content", "image", "category")        

    def save(self, owner, *tags) -> Article: # переопределяем метод
        article = Article.objects.create( # создание публикации
            **self.cleaned_data, # передача валидных данных с формы в публикацию
            owner = owner # определение владельца публикации
        )
        if tags: # если были переданы теги
            article.tags.add(*tags) # добавляем теги в публикацию

        return article
        
