from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.album_list, name='album-list'),
    path('show/<int:pk>/', views.album_detail, name='album-detail'),
    path('add/', views.album_create, name='album-create'),
    path('delete/<int:pk>/', views.album_delete, name='album-delete'),
]