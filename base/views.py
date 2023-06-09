from django.shortcuts import render
from django.http import HttpResponse
from .models import roomclass, device
import requests
from pytz import timezone
import pytz
from datetime import datetime

response = requests.get('https://openexchangerates.org/api/latest.json?app_id=650d1f1665d048869a1a174c95dd0275&symbols=CNY,GBP')

x = response.json()


me = 1/x['rates']['GBP'] * x['rates']['CNY']

print(x['rates']['GBP'])
print(x['rates']['CNY'])
print('------------------------')
print('BGP to CNY:  ', round(me, 4))


bigger_RMB = [
    # {'country':"CNY", 'name':'WangKai'},
    {'country':"GBP", 'rate': round(me, 4)},
    {'country':"USD", 'rate': x['rates']['CNY']},
]


def home(request):
    # room = roomclass.objects.all()

    context = {'rooms': bigger_RMB}
    return render(request, 'base/home.html', {'rooms': bigger_RMB, "device": device.objects.all()})


def money(request, pk):
    return render(request, "base/money.html")

def oest(request):
    return render(request, "base/oest.html")

def wangkai01(request):
    return render(request, "base/wangkai01.html", {'devices':device.objects.all})
