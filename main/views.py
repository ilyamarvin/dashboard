from django.db import connection
from django.db.models.aggregates import Avg
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.views.generic import ListView
from .forms import *

from main.models import Ads

menu = [{'title': 'Работники', 'url_name': 'about'},
        {'title': 'Добавить объявление', 'url_name': 'add_new'}, 
        {'title': 'Профиль', 'url_name': 'profile'}, 
        {'title': 'Вход и регистрация', 'url_name': 'register'}]


def index(request):
    ads = Ads.objects.all().order_by('id_ad')
    cats = Categories.objects.all()

    context = {
        'ads': ads,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'index.html', context)


def show_category(request, cat_id):
    ads = Ads.objects.filter(id_category=cat_id)
    cats = Categories.objects.all()

    if len(ads) == 0:
        raise Http404()

    context = {
        'ads': ads,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id,
    }

    return render(request, 'index.html', context)


def show_ad(request, ad_id):
    ad = get_object_or_404(Ads, id_ad=ad_id)
    context = {
        'ad': ad,
        'menu': menu,
        'title': ad.name,
        'cat_selected': ad.id_category,
        }
    return render(request, 'main/ad.html', context)


def add_ad(request):
    if request.method == 'POST':
        form = AddAdForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('main')
            except:
                form.add_error(None, 'Ошибка добавления объявления')
    else:
        form = AddAdForm()

    context = {
        'title': 'Создание объявления',
        'form': form,
        'menu': menu
    }
    return render(request, 'main/create_ad.html', context)


def profile(request):
    user = get_object_or_404(Users, username='nataly')
    ads = Ads.objects.filter(id_user=user.id_user).values('id_ad')
    rate = ReviewsOnUser.objects.filter(id_ad__in=ads).values('rating')
    rating = rate.aggregate(Avg('rating'))['rating__avg']
    
    context = {
        'user': user,
        'rate': rating,
        'menu': menu,
        'title': user.username
        }
    return render(request, 'profile.html', context)
    

def about(request):
    workers = Workers.objects.all()
    context = {
        'title': 'О сотрудниках',
        'menu': menu,
        'workers': workers
    }
    return render(request, 'main/about.html', context)


class SearchResultsList(ListView):
    model = Ads
    context_object_name = "ads"
    template_name = "index.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        ads = Ads.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if not ads:
            raise Http404("Ничего не нашлось... Попробуйте что-нибудь другое")
        else:
            return Ads.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )


def login(request):
    return HttpResponse('login page')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('main')
            except:
                form.add_error(None, 'Ошибка регистрации')
    else:
        form = RegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form,
        'menu': menu
    }
    return render(request, 'main/register.html', context)


def ad_update(request):
    return HttpResponse('update')


def delete_ad(request, ad_id):
    Ads.objects.get(id_ad=ad_id).delete()
    return redirect('main')


def write_review(request):
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('main')
            except:
                form.add_error(None, 'Ошибка добавления отзыва')
    else:
        form = AddReviewForm()

    context = {
        'title': 'Отзыв на объявление',
        'form': form,
        'menu': menu
    }
    return render(request, 'main/add_review.html', context)


def show_reviews(request):
    user = get_object_or_404(Users, username='nataly')
    ads = Ads.objects.filter(id_user=user.id_user).values('id_ad')
    reviews = ReviewsOnUser.objects.filter(id_ad__in=ads)
    
    context = {
        'user': user,
        'menu': menu,
        'title': "Отзывы пользователя" + user.username,
        'reviews': reviews
        }
    return render(request, 'main/reviews.html', context)