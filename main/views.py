from django.shortcuts import render, redirect
from django.http import HttpResponse
from .api_weather import make_request_name, make_request_hourly_city_id
from .image_select import image

def index(request):
    if request.method == 'POST':
        try:
            location = make_request_name(city_name= request.POST['city_name_input'])
            print('location data : ',location)
        except:
            print('city data not available')
        try:
            location_hourly = make_request_hourly_city_id(location['id'])
            print(location_hourly)
                # fetches the jason file of hourly forecast
        except:
            print('Hourly data not available')
        try:
            img = image(location['weather'][0]['icon'])
        except:
            img = ""
            print('image data not available')

        try:
            return render(request, 'location_result.html',
                          {'location': location,
                           'image_theme': img,
                           'details_hourly': location_hourly})
        except:
            return HttpResponse('Sorry, cannot show weather forecast.')
    else:
        return render(request, 'index.html', {})
