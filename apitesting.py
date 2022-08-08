#Weather query
import requests
def weather(location2):
        API_key="4e0be172ba5affd1c6fb97aceabe2940"
        location="Melbourne,AU"
        api_address=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_key}&units=metric"
        api_response=requests.get(api_address)
        api_to_dict=api_response.json()
        current_temp=api_to_dict['main']
        weather_desc=api_to_dict["weather"][0]["description"]

        print(f"Current temp is:{current_temp}, {weather_desc}")
        return(api_to_dict)

weather_stat=weather("melbourne")
# print(weather_stat["wind"])
# print(weather_stat["weather"])
print(weather_stat)