#!/usr/bin/python3.5

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Califonia': 'CA',
    'New Yeak': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New Yeak',
cities['OR'] = 'Portland'

print ('-' * 10)
print ("Michigan's abbre is :", states['Michigan'])
print ("Florida's abbre is :", states['Florida'])

print ('-' * 10)
for state, abbrev in states.items():
    print ("%s is abbre %s " % (state, abbrev))

print ('-' * 10)
for abbrev, city in cities.items():
    print ("%s has the city %s " % (abbrev, city))

print ('-' * 10)
for state, abbrev in states.items():
    print ("%s state is abbre %s and has city %s " % (state,abbrev,cities[abbrev]))

print ('-' * 10)
state = states.get('Texas', None)

if not states:
    print ("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exit')
print ("The city for the state 'TX' is: %s" % city)



    
    
    
    
    
    
    
    
    
    
    
    
