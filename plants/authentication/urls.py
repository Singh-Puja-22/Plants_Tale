from django.urls import path
from authentication import views

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
]