from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet, UserViewSet, api_route
from rest_framework import renderers
from . import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls))
]
