# Chapter 10. JSON
# Test commit
import json

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
print(name['prefix'], name['first'], name['last'])
