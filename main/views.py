from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse

from main.models import Ads


def index(request):
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM ads")
    # row = cursor.fetchall()
    # return HttpResponse(row)
    ads = Ads.objects.all()
    context = {
        'ads': ads
    }
    return render(request, 'example.html', context)


def ad(request, ad_id):
    ads = Ads.objects.filter(id_ad=ad_id)
    context = {
        'ads': ads
    }
    return render(request, 'example.html', context)

def about(request):
    return HttpResponse('about')