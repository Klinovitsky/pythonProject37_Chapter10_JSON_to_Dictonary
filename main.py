# Chapter 10. JSON

current = {'temperature': 67.2,
           'precip_prob': '40%'}

what_country = {'country': 'UK'}
loc = {'city': 'London'}
print('In',
      loc['city'] + ', ' + what_country['country'] + ' it is ' + str(current['temperature']),
      'degrees')
