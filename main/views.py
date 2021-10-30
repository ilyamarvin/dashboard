from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.views.generic import ListView

from main.models import Ads


def index(request):
    num_ads = Ads.objects.all().count()
    context = {
        'num_ads': num_ads
    }
    return render(request, 'index.html', context)


def ads(request):
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


def add(request):
    return HttpResponse('add new ad')


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
        return Ads.objects.filter(
            Q(name__icontains=query)
        )