from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ad/<int:ad_id>/', views.ad),
    path('about/', views.about),
]