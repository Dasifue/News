from rest_framework import serializers

from django.core.exceptions import ValidationError
from news.models import Article
from accounts.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only = ("id", "created", "updated")


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    class Meta:
        model = User
        exclude = ("is_superuser", "is_staff", "last_login")
        read_only = ("id", "is_active")

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")

        if password != password_confirm:
            raise ValidationError({"password": "Passwords did't match!"})

        return super().validate(attrs)
