# Chapter 10. JSON
import json

# Making a request to API
import requests

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if response.status_code == 200:
    print("Output from iss-now API:\n", response.text)
else:
    print("Houston, we have a problem:", response.status_code)


# Dictionaries
current = {'temperature': 67.2,
           'precip_prob': '40%'}

what_country = {'country': 'UK'}
loc = {'city': 'London'}
print('In',
      loc['city'] + ', ' + what_country['country'] + ' it is ' + str(current['temperature']),
      'degrees\n')


# From JSON into a dictionary
json_string = '{"first": "Emmett", "last": "Brown", "prefix": "Dr"}'
name = json.loads(json_string)
print("Print the dictionary:", name)
print("Output:", name['prefix'], name['first'], name['last'])
