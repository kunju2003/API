from django.shortcuts import render
import math,datetime,requests
from django.http import JaisonResponse
# Create your views here.
def index(request):
    city_name='kochi'
    if request.method=='POST':
        city_name=request.POST['city']
        print(city_name)
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=360e4bc3865e745ec844bd7ec054ca11'
    data=requests.get(url)
    weather_data=data.json()
    dt_object=datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    dt_object1=datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
    data={
        'date':dt_object.strftime('%d:%m:%y'),
        'city':city_name,
        'weather_discription':weather_data['weather'][0]['description'],
        'temperature_kelvin':weather_data['main']['temp'],
        'temperature_celsius':math.floor(weather_data['main']['temp']-273.15),
        'humidity':weather_data['main']['humidity'],
        'temp_min_celsius':math.floor(weather_data['main']['temp_min']-273.15),
        'temp_max_celsius':math.floor(weather_data['main']['temp_max']-273.15),
        'sunrise':dt_object.strftime('%H:%M:%S'),'sunset':dt_object1.strftime('%H:%M:%S'),
        'visibility':math.floor(weather_data['visibility']/1000),
        'cloud':weather_data['clouds']['all'],
        'wind':weather_data['wind']['speed'],
        'pressure':math.floor((weather_data['main']['pressure']/1013.25)*100),
        'feel_temp':math.floor(weather_data['main']['feels_like']-273.15),
        'sea_level':weather_data['main']['sea_level'],
        'grnd_level':weather_data['main']['grnd_level'],


    }
    return render(request,'index.html',{'data':data})


    def jsones(request):
        data-{
        "name":"jayalakshmi",
        "age":21,
        "city":True,
        }
        return JsonResponse(data)