from rest_framework import serializers
from blog.models import Article, Category
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login']


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    authorDetails = AuthorSerializers(source='author')

    class Meta:
        model = Article
        fields = ['id', 'authorDetails', 'category', 'title', 'description', 'content', 'coverImage', 'datetime', 'modified']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id', 'author', 'title', 'description', 'content', 'coverImage', 'datetime', 'modified']
        fields = '__all__'
