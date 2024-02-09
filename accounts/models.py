from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(verbose_name="Аватар", upload_to="avatars/", default="default/avatar.jpg", blank=True)
    email = models.EmailField(verbose_name="Почта", unique=True)
    biography = models.TextField(verbose_name="Биография", null=True, blank=True)
    job = models.CharField(verbose_name="Профессия", max_length=50, null=True, blank=True)
    favorites = models.ManyToManyField("news.Article", related_name="users", verbose_name="Фавориты", blank=True)
    is_active = models.BooleanField(verbose_name="Подтверждён", default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username} - {self.email}"
    
    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()