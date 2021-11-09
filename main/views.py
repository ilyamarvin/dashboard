from django.db import connection
from django.db.models.aggregates import Avg
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.views.generic import ListView
from .forms import *
from .models import *
from django.views.generic.edit import CreateView, UpdateView

from main.models import Ads

menu = [{'title': 'Работники', 'url_name': 'about'},
        {'title': 'Добавить объявление', 'url_name': 'ad_create'}, 
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


def ad_create(request):
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
    return render(request, 'main/ad_create.html', context)


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


def ad_update(request, ad_id):
    ad = get_object_or_404(Ads, id_ad=ad_id)
    form = UpdateAdForm(request.POST or None, instance = ad)
    if form.is_valid():
        try:
            form.save()
            return redirect('ad', ad_id=ad_id)
        except:
            form.add_error(None, 'Ошибка изменения объявления')
    
    context = {
        'title': f'Изменить объявление №{ad_id}',
        'form': form,
        'menu': menu
    }
    return render(request, 'main/ad_update.html', context)


def ad_delete(request, ad_id):
    Ads.objects.get(id_ad=ad_id).delete()
    return redirect('main')


def ad_reviews(request, ad_id):
    ad = get_object_or_404(Ads, id_ad=ad_id)
    reviews = ReviewsOnUser.objects.filter(id_ad = ad)
    print(reviews)
    context = {
        'menu': menu,
        'title': f"Отзывы на объявление {ad.name}",
        'reviews': reviews,
        'ad': ad
        }
    return render(request, 'main/ad_reviews.html', context)


def review_create(request, ad_id):
    ad = get_object_or_404(Ads, id_ad=ad_id)
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            try:
                form.instance.id_ad = ad
                form.save()
                return redirect('ad', ad_id=ad_id)
            except:
                form.add_error(None, 'Ошибка добавления отзыва')
    else:
        form = AddReviewForm()

    context = {
        'title': f'Отзыв на объявление {ad.name}',
        'form': form,
        'menu': menu
    }
    return render(request, 'main/review_create.html', context)


def show_reviews_user(request):
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

