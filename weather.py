import requests



def convert_kelvin_to_celsius(kelvin_temperature):
    return round(kelvin_temperature - 273.15, 2)

def Temp_Response():
    API_KEY = "e0f55f5da540796bf368cb531f905bf0"
    city_name = "Hyderabad"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_KEY}"

    response = requests.get(url).json()
    current_temperature_kelvin = response['main']['temp']
    feel = convert_kelvin_to_celsius(response['main']['feels_like'])
    temp_min = convert_kelvin_to_celsius(response['main']['temp_min'])
    temp_max = convert_kelvin_to_celsius(response['main']['temp_max'])
    weather=response["weather"][0]["description"]
    wind_speed = response['wind']['speed']
    wind_deg = response['wind']['deg']
    current_temperature_celsius = convert_kelvin_to_celsius(current_temperature_kelvin)
    temperature = "temperature is {} degree celsius".format(current_temperature_celsius)
    wea = "Now, temperature is {} degree celsius, feels like {} degree celsius, minimum temperature is {} , maximum temperature is {}, with {} , wind speed is {} kilometers per hour and in direction of {} degrees".format(current_temperature_celsius,feel,temp_min,temp_max,weather,wind_speed,wind_deg)
    #global temperature
    #global wea
    return (temperature,wea)