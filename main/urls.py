from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('ads/', views.ads, name='ads'),
    path('ad/<int:ad_id>/', views.ad),
    path('add/', views.add_ad, name='add_new'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('personal/', views.personal, name='personal'),
    path('search/', views.SearchResultsList.as_view(), name='search_results'),
    path('ad_delete/', views.DeleteAd.as_view(), name='ad_delete'),
    path('ad_update/', views.ad_update, name='ad_update'),
]