import requests

def get_weather(city, api_key):
    # API endpoint URL
    url = f"http://openweathermap.org{city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            print(f"\n--- Weather in {city.capitalize()} ---")
            print(f"Temperature: {main['temp']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Condition: {weather['description'].capitalize()}")
        else:
            print(f"City '{city}' not found.")
            
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    MY_API_KEY = "your_api_key_here"  # Replace with your actual key
    user_city = input("Enter city name: ")
    get_weather(user_city, MY_API_KEY)
