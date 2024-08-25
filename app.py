import requests

api_key = 'f36d6c41d195c3f4e20d16bbdaee4470'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}"
)

if weather_data.json()['cod'] == '404':
    print("Sorry, can't find that city. Please check if you have spelt it correctly")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(weather, temp)

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp} degrees celcius")

