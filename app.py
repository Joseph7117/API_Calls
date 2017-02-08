import requests
# Ask the User to Enter the City whose weather is required
city = input("Please Enter the City to find the Temperature details (e.g Nairobi, London, New York) ?")

def determine_weather():

    #Make a HTTP request to the Open Weather API
    api_key = '452954947f855c583109385c3c5b532f'
    request_made = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key)

    #Read the JSON forwarded by server
    weather_json_object = request_made.json()
    temperature_kelvins = float(weather_json_object['main']['temp'])

    #cast the temperature to String type
    temperature_kelvins_str = str(temperature_kelvins)

    #Format the JSON to make it readable on the terminal
    print("Temperature in "+city+" is "+temperature_kelvins_str+" kelvins")


if city in ['Nairobi', 'Lagos', 'London', 'New York', 'Delhi']:
    determine_weather()
else:
    print("Enter a Valid City\n")
    exit(0)