from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.AlbumListView.as_view(), name='album-list'),
    path('show/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
    path('add/', views.AlbumCreateView.as_view(), name='album-create'),
    path('delete/<int:pk>/', views.AlbumDeleteView.as_view(), name='album-delete'),
]
