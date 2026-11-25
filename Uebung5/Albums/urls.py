from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.album_list, name='album-list'),
    path('show/<int:pk>/', views.album_detail, name='album-detail'),
]