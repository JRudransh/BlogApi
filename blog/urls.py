from django.urls import path, include
from blog.views import ArticleViewSet, UserViewSet, CategoryViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
router.register('user', UserViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
