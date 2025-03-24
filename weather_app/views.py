from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def weather_app(request):
    if request.method == 'POST':
        name = request.POST['city']
        api_key = "71df1535d7f8fae997f84dd67ac5c4ff"

        # Correct URL formatting
        url = f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}"

        # Fetch data
        source = urllib.request.urlopen(url).read()
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "city":name,
            "country_code": "IN",
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(round(list_of_data['main']['temp'] - 273.15, 2)) + '°C',  # Convert Kelvin to Celsius
            "pressure": str(list_of_data['main']['pressure']) + ' hPa',
            "humidity": str(list_of_data['main']['humidity']) + '%',
        }
        print(data)
    else:
        data = {}
    return render(request, "weather_app/index.html", data)