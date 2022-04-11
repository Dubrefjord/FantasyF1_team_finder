import requests
import json

drivers = []
constructors = []

r = requests.get('https://fantasy-api.formula1.com/f1/2022/players')
driver_data = r.json()
for player in driver_data['players']:
    if player['position'] == 'Constructor':
        constructors.append((player['team_abbreviation'],player['price']))
        continue
    driver_abbreviation = player['last_name'][0:3]
    drivers.append((driver_abbreviation,player['price']))

drivers.sort(reverse=True, key=lambda tup: tup[1])
constructors.sort(reverse=True, key=lambda tup: tup[1])

num_drivers = len(drivers)
result=[] #structure = (drivers,cost)
for constructor in constructors:
    for first in range(0,(num_drivers-4)):
        for second in range(first+1,(num_drivers-3)):
            for third in range(second+1,(num_drivers-2)):
                for fourth in range(third+1,(num_drivers-1)):
                    for fifth in range(fourth+1,num_drivers):
                        result.append((drivers[first][0]+', '+drivers[second][0]+', '+drivers[third][0]+', '+drivers[fourth][0]+', '+drivers[fifth][0]+' : '+constructor[0],drivers[first][1]+drivers[second][1]+drivers[third][1]+drivers[fourth][1]+drivers[fifth][1]+constructor[1]))
                    
result.sort(reverse=True, key=lambda tup: tup[1])

file = open('F1FantasyTeams.txt','w')
for tuple in result: # tuple looks like (<list of drivers names and constructor>,cost) use filters below to remove unnecessary results.
    if not 'Str' in tuple[0] and not 'Lat' in tuple[0] and 'FER' in tuple[0] and tuple[1]>95 and tuple[1]<105:
        file.write(tuple[0]+'  '+str(round(tuple[1],1))+'\n')