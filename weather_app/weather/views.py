from django.shortcuts import render
import requests
import datetime
# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Khulna'


    appid = '1164e059f544e61bc0ea04b66c610b14'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL,params=PARAMS)
    res = r.json()
    description=res['weather'][0]['description']
    icon=res['weather'][0]['icon']
    temp=res['main']['temp']
    temp_min=res['main']['temp_min']
    temp_max=res['main']['temp_max']
    feels_like=res['main']['feels_like']
    humidity=res['main']['humidity']
    visibility=res['visibility']
    pressure=res['main']['pressure']
    speed=res['wind']['speed']
    day = datetime.date.today()
    return render(request, 'index.html',{'description':description, 'speed':speed, 'visibility':visibility, 'feels_like':feels_like, 'icon':icon, 'temp':temp, 'temp_min':temp_min, 'humidity':humidity, 'temp_max':temp_max,'pressure':pressure, 'day':day, 'city':city})
