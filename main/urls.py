from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('ad/<int:ad_id>/', views.show_ad, name='ad'),
    path('ad/<int:ad_id>/delete/', views.ad_delete, name='ad_delete'),
    path('ad/<int:ad_id>/update/', views.ad_update, name='ad_update'),
    path('ad/<int:ad_id>/reviews/', views.ad_reviews, name='ad_reviews'),
    path('ad/<int:ad_id>/review_create/', views.review_create, name='review_create'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('ad/create', views.ad_create, name='ad_create'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/nataly/', views.profile, name='profile'),
    path('search/', views.SearchResultsList.as_view(), name='search_results'),
    path('profile/nataly/reviews/', views.show_reviews_user, name='reviews'),
]