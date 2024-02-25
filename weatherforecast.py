import requests

def get_weather(city):
    
    api_key = 'API_KEY'
    url = f'bf759e135a83ea2c3ce7982e39a2d1cc'
    response = requests.get(url)
    data = response.json()
    return data

def main():
    city = input("Enter the name of a city: ")
    weather_data = get_weather(city)
    
    if weather_data['cod'] == 200:  # Check if the request was successful
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
