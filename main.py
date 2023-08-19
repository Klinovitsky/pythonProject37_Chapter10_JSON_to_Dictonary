# Chapter 10. JSON. I. Space Station is traveling at 4.75 miles per second (4.75mi/s= 27519.78kph)

# Imports from different modules should occur on different lines.
# Anti-pattern here:
# import requests, json
import requests
import json
import turtle


# Take coordinates and move the turtle (ISS) on the map
def move_iss(lat, long):
    global iss

    iss.penup()
    iss.goto(long, lat)
    iss.pendown()


# Screen object (Turtle)
screen = turtle.Screen()
screen.setup(1000, 500)
screen.bgpic('earth.gif')
# setworldcoordinates - method, set coordinate system of the turtles to match that of the Earth
screen.setworldcoordinates(-180, -90, 180, 90)  # Reset the grid system. Match the earth coordinates

# Represent the location of the ISS over the earth
iss = turtle.Turtle()
turtle.register_shape("iss.gif")
iss.shape("iss.gif")
# iss.shape('circle')
# iss.color('red')

# Making a request to API and use "loads" function to convert data to a dictionary
url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if response.status_code == 200:
    response_dictionary = json.loads(response.text)     # take response in string form
    print("Output from iss-now API:", response.text)
    print("Output from the dictionary:", response_dictionary)
    position = response_dictionary['iss_position']
    print('International Space Station at ' + position['latitude'] + ', ' + position['longitude'])
    # Get latitude and longitude from the dictionary
    lat = float(position['latitude'])
    long = float(position['longitude'])
    move_iss(lat, long)     # Pass lat and long to function

else:
    print("Houston, we have a problem:", response.status_code)

turtle.mainloop()   # Display the turtle window

# Exercise. Dictionaries
current = {'temperature': 67.2,
           'precip_prob': '40%'}

what_country = {'country': 'UK'}
loc = {'city': 'London'}
print('In',
      loc['city'] + ', ' + what_country['country'] + ' it is ' + str(current['temperature']),
      'degrees\n')


# Exercise. From JSON into a dictionary
json_string = '{"first": "Emmett", "last": "Brown", "prefix": "Dr"}'
name = json.loads(json_string)
print("Print the dictionary:", name)
print("Output:", name['prefix'], name['first'], name['last'])
