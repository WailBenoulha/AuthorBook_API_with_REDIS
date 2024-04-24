# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorAPI, BookAPI, RelationAPI


urlpatterns = [
    path('author/',AuthorAPI.as_view(),name='author'),
    path('book/',BookAPI.as_view(),name='book'),
    path('relation/',RelationAPI.as_view(),name='relation')
]
