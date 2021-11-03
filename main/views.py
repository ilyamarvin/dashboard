from django.db import connection
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.views.generic import ListView
from .forms import *

from main.models import Ads


def index(request):
    num_ads = Ads.objects.all().count()
    context = {
        'num_ads': num_ads,
        'title': 'Главная страница'
    }
    return render(request, 'index.html', context)


def ads(request):
    ads = Ads.objects.all()
    context = {
        'ads': ads,
        'title': 'Все объявления'
    }
    return render(request, 'main/ads.html', context)


def ad(request, ad_id):
    if ad_id > len(Ads.objects.all()) or ad_id <= 0:
        raise Http404("Такого объявления не существует... Попробуйте что-нибудь другое")
    else:
        ads = Ads.objects.filter(id_ad=ad_id)
        context = {
        'ads': ads,
        'title': f'Объявление №{ ad_id }'
    }
    return render(request, 'main/ads.html', context)


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
        'form': form
    }
    return render(request, 'main/create_ad.html', context)


def personal(request):
    return HttpResponse('personal information')
    

def about(request):
    return HttpResponse('about')

class SearchResultsList(ListView):
    model = Ads
    context_object_name = "ads"
    template_name = "main/ads.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        ads = Ads.objects.filter(Q(name__icontains=query))
        if not ads:
            raise Http404("Ничего не нашлось... Попробуйте что-нибудь другое")
        else:
            return Ads.objects.filter(
                Q(name__icontains=query)
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
        'form': form
    }
    return render(request, 'main/register.html', context)


def delete_ad(request):
    return HttpResponse('haha delete')