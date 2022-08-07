#Weather query
import requests
def weather(location2):
        API_key="4e0be172ba5affd1c6fb97aceabe2940"
        location="Melbourne,AU"
        api_address=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_key}&units=metric"
        api_response=requests.get(api_address)
        api_to_dict=api_response.json()
        current_temp=api_to_dict['main']['temp']
        print(f"current temp is:{current_temp}")
        return()

weather_stat=weather("melbourne")
print(weather_stat)