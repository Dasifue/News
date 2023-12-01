from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name



class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name="Владелец")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="articles", null=True, blank=False, verbose_name="Категория")
    name = models.CharField(verbose_name="Заголовок", max_length=100)
    content = models.TextField(verbose_name="Контент")
    image = models.ImageField(verbose_name="Изображение", upload_to="articles/", null=True, blank=True)
    created = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    
    def __str__(self):
        return self.name