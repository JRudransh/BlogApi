from blog.models import Article, Category
from rest_framework import viewsets, permissions

from blog.pagination import DefaultPagination
from blog.permission import IsOwnerOrReadOnly
from blog.serializers import ArticleSerializer
from blog.serializers import UserSerializers
from blog.serializers import CategorySerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializers


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = DefaultPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
