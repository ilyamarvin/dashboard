from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, Http404

from main.models import Ads


def index(request):
    ads = Ads.objects.all()
    context = {
        'ads': ads
    }
    return render(request, 'main/ads.html', context)


def ad(request, ad_id):
    if ad_id > len(Ads.objects.all()) or ad_id <= 0:
        raise Http404("Такого объявления не существует... Попробуйте что-нибудь другое")
    else:
        ads = Ads.objects.filter(id_ad=ad_id)
        context = {
        'ads': ads
    }
    return render(request, 'main/ads.html', context)
    

def about(request):
    return HttpResponse('about')