from . import views
from django.urls import path


app_name = "cart"
urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:plant_id>/', views.add_to_cart, name='add_to_cart'),
    path('buy/<int:plant_id>/', views.buy_now, name='buy_now'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]