from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('ad/<int:ad_id>/', views.show_ad, name='ad'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('add/', views.add_ad, name='add_new'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/nataly/', views.profile, name='profile'),
    path('search/', views.SearchResultsList.as_view(), name='search_results'),
    path('ad_delete/<int:ad_id>/', views.delete_ad, name='ad_delete'),
    path('ad_update/', views.ad_update, name='ad_update'),
    path('review/', views.write_review, name='review'),
]