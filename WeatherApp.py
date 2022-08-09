#Amal Kariyawasam, WeatherApp using OpenWeatherMap

from flask import Flask, render_template, request # import what we need to use from the flask library
import requests
app = Flask(__name__) # invoke the Flask class
#API Key: 4e0be172ba5affd1c6fb97aceabe2940 


#Function to query Weather API and to return data 
def weather(location_input): # Define function
        API_key="4e0be172ba5affd1c6fb97aceabe2940" # API Key from Openweather MAP
        api_address=f"https://api.openweathermap.org/data/2.5/weather?q={location_input}&appid={API_key}&units=metric" # Query to get the weather
        api_response=requests.get(api_address) # Save response into a variable
        api_to_dict=api_response.json() # Convert the API response into a Python Dictionary
        weather_desc=api_to_dict["weather"][0]["description"]
        current_temp=api_to_dict["main"]["temp"] # Save the current temprature from the dictionary
        weather_feels=api_to_dict["main"]["feels_like"]
        pressure=api_to_dict["main"]["pressure"]
        humidity=api_to_dict["main"]["humidity"]
        selected_location=api_to_dict["name"]
        selected_country=api_to_dict["sys"]["country"]


        return(f"{selected_location}, {selected_country} is {weather_desc} and tempreature is:{current_temp} Degrees and it feels like {weather_feels} Degrees.\n Pressure is:{pressure} hpa and humidity is:{humidity}%, have an awesome day !") # Return this to function


# Following function will declare the index function and call index.html and the weather () function
@app.route("/",methods=["GET"])
def main_route():
    return render_template("index.html", weather=weather("Melbourne,au"))

# Following function will get the the location from URL and try to pass this to the weather() function
@app.route("/<location>",methods=["GET"])
def weather_by_location(location):
    return render_template("index.html",weather=weather(location))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="100", debug=True) # Start the server listening for requests