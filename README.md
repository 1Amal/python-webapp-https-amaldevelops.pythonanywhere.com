# Python_Flask_Weather_App
 Python Flask Weather App
Live version of this app can be accessed from https://amaldevelops.pythonanywhere.com/


Usage

    Default weather location is set as Melbourne, Australia
    To get any location enter ["/city_name,two digit country code"] infront of the base URL.
    I.e. for Colombo, LK enter https://amaldevelops.pythonanywhere.com/colombo,lk

Technology stack and how this app work !

Front end code for this web app is written in;

    HTML, (HyperText Markup Language) is the code that is used to structure this web page and its content
    CSS, (Cascading Style Sheets) is a stylesheet language used to describe the presentation of this document written in HTML
    Jinja, is a full-featured template engine for Python that is used to pass Python variables to the HTML web page

Back end code for this web app is written in;

    Python, a high-level, interpreted, general-purpose programming language.
    Its design philosophy emphasises code readability with the use of significant indentation.
    Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural),object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library
    Flask, is a lightweight WSGI web application framework
    OpenWeatherMap API, is used to receive Weather data
    Python Anywhere, is used to host this Webapp which allows you to host, run, and code Python in the cloud, which is pretty cool!

How this app work ?

    When a user enters the web app URL i.e. https://amaldevelops.pythonanywhere.com it will call the main route in the Python code.
    Default behaviour of the Main route in the Python/flask code is programmed so it will give "Melbourne,Australia" weather information by calling up the main function and will pass the location as a variable to the function, which contains code to call the OpenWeathermap API.
    Using the following format we can call the API using this format with a GET request: [https://api.openweathermap.org/data/2.5/weather?q={location_input}&appid={API_key}&units=metric]
    {location_input} is passed from the user entered location along with {API_key} supplied by openweathermap.[&units=metric] is used to specify the unit of measurement we need.
    In response Openweathermap will send a response in JSON format
    A function written in Python will convert JSON format to a Python Dictionary and we can then manipulate the data as we wish.
    Using Python dictionary methods we can extract the information we require and all required weather data is stored in a Python variable in text format.
    Above Python variable is passed to Flask and it is parsed by Flask along with HTML/Jinja template and CSS.
    Flask will interpret the HTML,CSS,Jinja,Python code and will create a new HTML document which will be pushed back to the users browser as can be seen on this webpage.

