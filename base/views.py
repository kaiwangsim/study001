from django.shortcuts import render
from django.http import HttpResponse
from .models import roomclass
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





fmt = '%Y-%m-%d %H:%M:%S %Z%z'
zone_CN = timezone('Asia/Shanghai')
zone_London = timezone('Europe/London')
CN_time=datetime.now().astimezone(zone_CN).strftime(fmt)
London_time=datetime.now().astimezone(zone_London).strftime(fmt)
# test12= [CN_time, London_time]
test12= [{'country': 'China', 'time': CN_time},
         {'country': 'London', 'time': London_time},
         ]

# Create your views here.
def home(request):
    # room = roomclass.objects.all()

    context = {'rooms': bigger_RMB}
    return render(request, 'base\home.html', {'rooms': bigger_RMB, 'test11': test12})


def money(request, pk):
    return render(request, "base\money.html")

def oest(request):
    return render(request, "base\oest.html")

