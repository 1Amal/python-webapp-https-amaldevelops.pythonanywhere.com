#Weather query
import requests
#Function to query Weather API and to return data 

def weather(location_input): # Define function
        API_key="4e0be172ba5affd1c6fb97aceabe2940" # API Key from Openweather MAP
        api_address=f"https://api.openweathermap.org/data/2.5/weather?q={location_input}&appid={API_key}&units=metric" # Query to get the weather
        api_response=requests.get(api_address) # Save response into a variable
        api_to_dict=api_response.json() # Convert the API response into a Python Dictionary
        status_code=api_to_dict["cod"] # This will check the API response code, 200=City found 404=City not found

        #Following code will runfor Correct location
        if status_code==200:
                weather_desc=api_to_dict["weather"][0]["description"] ## This will give output of weather atrribute "Description of the weather"
                current_temp=api_to_dict["main"]["temp"] # Save the current temprature from the dictionary
                weather_feels=api_to_dict["main"]["feels_like"] # This will give output of weather atrribute "Feels like"
                pressure=api_to_dict["main"]["pressure"] # This will give output of weather atrribute "Pressure"
                humidity=api_to_dict["main"]["humidity"] # This will give output of weather atrribute "Humidity"
                selected_location=api_to_dict["name"] # This will give output of currently selected "city name"
                selected_country=api_to_dict["sys"]["country"] # This will give output of currently selected "Country with two digit country code"
                
                # Below variable will save all weather data to final_output variable
                final_output=f"{selected_location}, {selected_country} is {weather_desc} and tempreature is:{current_temp} Degrees and it feels like {weather_feels} Degrees.\n Pressure is:{pressure} hpa and humidity is:{humidity}%, have an awesome day !"
        
        # Following code will run for incorrect data
        else:
                final_output=f"Incorrect city, please try again!"
        
        #This will return data saved in variable "final_output"
        return (final_output) 

print(weather("colombo,lk"))
# print(weather_stat["wind"])
# print(weather_stat["weather"])
# print(weather_stat)

# https://api.openweathermap.org/data/2.5/weather?q=melbourne&appid=4e0be172ba5affd1c6fb97aceabe2940&units=metric

# Response for succesful location: {"coord":{"lon":-80.6081,"lat":28.0836},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
# "base":"stations","main":{"temp":29.4,"feels_like":34.7,"temp_min":28.35,"temp_max":30.59,"pressure":1019,"humidity":75},"visibility":10000,"wind":{"speed":6.17,"deg":120,"gust":9.77},"clouds":{"all":0},"dt":1660174378,"sys":{"type":2,"id":2007578,"country":"US","sunrise":1660128589,"sunset":1660176352},"timezone":-14400,"id":4163971,"name":"Melbourne","cod":200}

#Error code for not found location: {"cod":"404","message":"city not found"}