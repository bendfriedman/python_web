from django.urls import path
from HolidayHousings import views


urlpatterns = [
    path('show/', views.housing_list, name='housing-list'),
    path('show/<int:pk>', views.housing_detail, name='housing-detail'),
    path('add/', views.housing_create, name='housing-create')
]