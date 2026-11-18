from django.urls import path
from app_my_cool_website import views

urlpatterns = [
    path('', views.home, name='home'),
]