from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('ads/', views.ads, name='ads'),
    path('ad/<int:ad_id>/', views.ad),
    path('add/', views.add, name='add_new'),
    path('about/', views.about, name='about'),
    path('personal/', views.personal, name='personal'),
    path('search/', views.SearchResultsList.as_view(), name='search_results')
]