from django.urls import path

from app import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('list', views.PlantList.as_view(), name='list'),
    path('plantdetail/<int:pk>', views.PlantDetail.as_view(), name='plantdetail'),
]