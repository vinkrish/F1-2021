races = [
    'bahrain-gp',
    'emilia-romagna-gp',
    'portuguese-gp',
    'spanish-gp',
    'monaco-gp',
    'azerbaijan-gp',
    'french-gp',
    'styrian-gp',
    'austrian-gp',
    'british-gp',
    'hungarian-gp',
    'belgian-gp',
    'dutch-gp',
    'italian-gp',
    'russian-gp',
    'turkish-gp',
    'united-states-gp',
    'mexican-gp',
    'brazilian-gp',
    'qatar-gp',
    'saudi-arabia-gp',
    'abu-dhabi-gp'
]

def checkKey(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

# dictionary of car and results among driver of those car extracted
race_dict = {}
for i in range(len(races)):
    car_dict = {}
    with open('race/race_'+races[i]+'.txt') as f:
        for result in f:
            values = result.split(',')
            try:
                hours, minutes =  values[8].split(":") 
                minutes, seconds =  minutes.split("'") 
                seconds, milliseconds = seconds.split(".")
                ms = int(3600000 * int(hours) + 60000 * int(minutes) + 1000 * int(seconds) + int(milliseconds))
            except:
                ms = 0
            info = {'car_number': values[2], 'driver_name': values[3], 'qualified_time': ms}
            if checkKey(car_dict, values[5]):
                car_dict[values[5]].append(info)
            else:
                car_dict[values[5]] = [info]
    if races[i] != 'belgian-gp':
        race_dict[races[i]] = car_dict
    
# calculate time difference between drivers of same car
race_winners = {}
for i in range(len(races)):
    winners = []
    if races[i] != 'belgian-gp':
        car_dict = race_dict[races[i]]
        for car, info in car_dict.items():
            driver_1 = info[0]
            driver_2 = info[1]
            winner = {'driver_name': driver_1['driver_name'], 'time_diff': driver_2['qualified_time'] - driver_1['qualified_time']}
            if car != 'Haas':
                winners.append(winner)
    race_winners[races[i]] = winners

# findig winners in each race
for i in range(len(races)):
    if races[i] != 'belgian-gp':
        winners = race_winners[races[i]]
        winners_sorted = sorted(winners, key = lambda i: i['time_diff'],reverse=True)
        winners_filtered = [w for w in winners_sorted if w['time_diff'] < 60000]
        with open('race_winners.txt', 'a') as file:
            file.write(races[i] + ':' + winners_filtered[0]['driver_name'] + ',' + str(winners_filtered[0]['time_diff']) +'\n')