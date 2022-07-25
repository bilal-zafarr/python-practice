import requests
import json

def get_weather(city, units, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)
    weather = json.loads(response.text)
    return weather

def main():
    print("\n------------------------------------------------")
    print("\tWelcome to Weather App")
    print("------------------------------------------------\n")

    api_key = "553a776215939673ca33edb09bd82a19"
    city = input("Enter city name: ")

    print("\n-> Enter 1 for Celsius")
    print("-> Enter 2 for Farenheit")
    print("-> Enter any other key to quit the program\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        units = "metric"
    elif choice == "2":
        units = "imperial"
    else:
        print("Bye bye!")
        return

    print("\n-> Enter 1 if you want to get the short weather description.")
    print("-> Enter 2 if you want to get detailed weather")
    print("-> Enter any other key to quit the program\n")
    choice = input("Enter your choice: ")

    weather = get_weather(city, units, api_key)

    if choice == "1":
        print("\n\t****Current Weather****\n")
        print("City: ", weather["name"])
        print("Temperature: ", weather["main"]["temp"])
        print("Description: ", weather["weather"][0]["description"])
    elif choice == "2":
        print("\n\t****Current Weather****\n")
        print("City: ", weather["name"])
        print("Temperature: ", weather["main"]["temp"])
        print("Description: ", weather["weather"][0]["description"])
        print("Humidity: ", weather["main"]["humidity"])
        print("Pressure: ", weather["main"]["pressure"])
        print("Wind Speed: ", weather["wind"]["speed"])
        print("Wind Direction: ", weather["wind"]["deg"])
    else:
        print("Bye bye!")
        return

    print("\n------------------------------------------------")
    print("\tThank you for using Weather App")
    print("------------------------------------------------\n")

if __name__ == "__main__":
    main()
    