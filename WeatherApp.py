#Amal Kariyawasam, Assignment 3

from flask import Flask, render_template, request # import what we need to use from the flask library
import requests
app = Flask(__name__) # invoke the Flask clas
#API Key: 4e0be172ba5affd1c6fb97aceabe2940 


#Weather query function
def weather(location_input): # Define function
        API_key="4e0be172ba5affd1c6fb97aceabe2940" # API Key from Openweather MAP
        # location_input=location
        api_address=f"https://api.openweathermap.org/data/2.5/weather?q={location_input}&appid={API_key}&units=metric" # Query to get the weather
        api_response=requests.get(api_address) # Save response onto variable
        api_to_dict=api_response.json() # Convert the API response into a Python Dictionary
        current_temp=api_to_dict['main']["temp"] # Save the current temprature from the dictionary
        weather_desc=api_to_dict["weather"][0]["description"]
        return(f"Current temperature in {location_input}, is {current_temp} C, it is {weather_desc}") # Return this to function


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