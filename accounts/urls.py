from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('dashboard/<int:pk>', views.dashboard, name = 'dashboard'),
]