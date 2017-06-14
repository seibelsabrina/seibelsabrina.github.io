import json
import urllib.request

#Uses metaweather's API to give JSON data for weather

def get_data(url):
    print("sending a request to {}".format(url))
    data = urllib.request.urlopen(url).read().decode()
    return json.loads(data)

def get_weather(long,lat):
    # documentation www.metaweather.com/api
    url = "https://www.metaweather.com/api/location/search/?lattlong={},{}".format(long,lat)
    cities = get_data(url)
    if len(cities)== 0:
      return"No cities close by"
    closest_city = cities[0]
    print("City: {}, ID:{}".format(closest_city["title"],closest_city["woeid"]))
    city_id = closest_city["woeid"]
    url = "https://www.metaweather.com/api/location/{}".format(city_id)
    weather_info = get_data(url)
    weather_list = weather_info["consolidated_weather"]
    temp = weather_list[0]['the_temp']
    temp = temp*1.8 + 32 
    print("The tempurature is {:2f} degrees farenheit.".format(temp))
    weather_description = weather_info['consolidated_weather'][0]['weather_state_name']
    print('It is currently {} outside.'.format(weather_description))
