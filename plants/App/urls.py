from django.urls import path

from app import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('add', views.PlantCreate.as_view(), name='add'),
    path('list', views.PlantList.as_view(), name='list'),
    path('plantdetail/<int:pk>', views.PlantDetail.as_view(), name='plantdetail'),
    
    path('editplant/<int:pk>', views.EditPlant.as_view(), name='editplant'),
    path('deleteplant/<int:pk>', views.DeletePlant.as_view(), name='deleteplant'),

    path('search/', views.search, name='search'),
]