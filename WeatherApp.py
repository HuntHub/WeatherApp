from urllib.request import HTTPPasswordMgrWithDefaultRealm
import requests, datetime

#defines function that outputs a category of wind speed based on how fast the wind is
def windcategory(wind_speed):
  if (wind_speed == 0):
    output ='Calm'
  if (wind_speed > 0) and (wind_speed <= 3):
    output ='Light air'
  if (wind_speed > 3) and (wind_speed <= 7):
    output ='Light breeze'
  if (wind_speed > 7) and (wind_speed <= 12):
    output ='Gentle breeze'
  if (wind_speed > 12) and (wind_speed <= 18):
    output ='Moderate breeze'
  if (wind_speed > 18) and (wind_speed <= 24):
    output ='Fresh breeze'
  if (wind_speed > 24) and (wind_speed <= 31):
    output ='Strong breeze'
  if (wind_speed > 31) and (wind_speed <= 38):
    output ='Near gale'
  if (wind_speed > 38) and (wind_speed <= 46):
    output ='Gale'
  if (wind_speed > 46) and (wind_speed <= 54):
    output ='Strong gale'
  if (wind_speed > 54) and (wind_speed <= 63):
    output ='Whole gale'
  if (wind_speed > 63) and (wind_speed <= 75):
    output ='Storm force'
  if (wind_speed > 75):
    output ='SEEK SHELTER - HURRICANE FORCE WINDS'
  return output

def new_func():
    output = ""

#conditional logic to tell us what we should wear based on the temperature
def clothingfunct(temperature):
  if temperature <= 65:
    output = 'Wear a coat!'
  if (temperature >= 66) and (temperature <= 91):
    output = 'Wear shorts'
  if temperature >= 92:
    output = 'Live elsewhere'
  return output

#conditional logic to tell us how humid the air is
def humidityfunct(humidity):
  if humidity <= 40:
    output = 'Air is good'
  if (humidity > 40) and (humidity <= 65):
    output = 'Average humidity'
  if humidity > 65:
    output = 'The air is thicc'
  return output


#assigns the degree symbol to a variable
degree_sign = u'\N{DEGREE SIGN}'


#prompts user for input of a city name
city_name = input("Type your city: ")

print()
print()


# creates a response variable by taking the user input and putting it in the api call to retrieve json data that is then converted from Kelvin to Fahrenheit
response = requests.get("https://api.openweathermap.org/data/2.5/weather?appid=c8efac34cc3548754ca009222d24da49&q=" + city_name + "&units=imperial").json()


#creates variables to define with JSON data from API call and in some cases converts the data
daily_max_temp = response['main'].get('temp_max')
daily_min_temp = response['main'].get('temp_min')


temperature = response['main'].get('temp')
feels_like = response['main'].get('feels_like')
humidity = response['main'].get('humidity')


sunrise = response['sys'].get('sunrise')
sunrise_time = datetime.datetime.fromtimestamp(sunrise, datetime.timezone(datetime.timedelta(hours = -4)))


sunset = response['sys'].get('sunset')
sunset_time = datetime.datetime.fromtimestamp(sunset, datetime.timezone(datetime.timedelta(hours = -4)))

sky_status = response['weather'][0].get('description')
wind_speed = response['wind'].get('speed')


#prints the desired values
categoryspeed = windcategory(wind_speed)
print(sky_status.capitalize())
print(categoryspeed, wind_speed, 'mph', '\n\n')


print('Daily maximum temperature =', daily_max_temp, (degree_sign) + 'F')
print('Daily minimum temperature =', daily_min_temp, (degree_sign) + 'F', '\n\n')


print('Currently', temperature , (degree_sign) + 'F')
print('Feels like', feels_like , (degree_sign) + 'F')
print(str(humidity) + '% humidity','\n\n')


print('Sunrise', str(sunrise_time)[12:19:])
print('Sunset', str(sunset_time)[12:19:], '\n\n')

print(clothingfunct(temperature))
print(humidityfunct(humidity))

'''

#Kelvin to Fahrenheit conversion. Openweather API conversion broken.
def tempconvert(kelvin):
    return kelvin * 1.8 - 459.67


kelvin = temperature2
converted = tempconvert(kelvin)
print(temperature2)

'''