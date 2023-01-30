from django.shortcuts import render
import requests
import json

my_api = '9e73abaccd4b204983168d955c608293'


def home(request):
	if request.method == "POST":
			city = request.POST.get('city')
			url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={my_api}"
			list_of_data = requests.get(url).json()

			data = {
				"country_code": str(list_of_data['sys']['country']),
	            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
	            "temp": str(list_of_data['main']['temp']) + 'k',
	            "pressure": str(list_of_data['main']['pressure']),
	            "humidity": str(list_of_data['main']['humidity']),
	            'main': str(list_of_data['weather'][0]['main']),
	            'description': str(list_of_data['weather'][0]['description']),
	            'icon': list_of_data['weather'][0]['icon'],
	            'city': city
			}

	else:
		data = {}



	return render(request, "home.html", data)
