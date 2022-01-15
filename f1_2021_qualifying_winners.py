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

sprint_races = ['british-gp', 'italian-gp', 'brazilian-gp']

# dictionary of car and results among driver of those car extracted
qualifying_dict = {}
for i in range(len(races)):
    car_dict = {}
    with open('qualifying/qualifying_'+races[i]+'.txt') as f:
        for result in f:
            values = result.split(',')
            try:
                if races[i] in sprint_races:
                    qualifying_time = values[7]
                else:
                    qualifying_time = values[6]
                minutes, seconds =  qualifying_time.split("'") 
                seconds, milliseconds = seconds.split(".")
                ms = int(60000 * int(minutes) + 1000 * int(seconds) + int(milliseconds))
            except:
                ms = 0
            info = {'car_number': values[1], 'driver_name': values[2], 'qualified_time': ms}
            if checkKey(car_dict, values[4]):
                car_dict[values[4]].append(info)
            else:
                car_dict[values[4]] = [info]
    qualifying_dict[races[i]] = car_dict

# calculate time difference between drivers of same car
qualifying_winners = {}
for i in range(len(races)):
    winners = []
    car_dict = qualifying_dict[races[i]]
    for car, info in car_dict.items():
        driver_1 = info[0]
        driver_2 = info[1]
        winner = {'driver_name': driver_1['driver_name'], 'time_diff': driver_2['qualified_time'] - driver_1['qualified_time']}
        if car != 'Haas':
            winners.append(winner)
    qualifying_winners[races[i]] = winners

# findig winners in each race
for i in range(len(races)):
    winners = qualifying_winners[races[i]]
    winners_sorted = sorted(winners, key = lambda i: i['time_diff'],reverse=True)
    winners_filtered = [w for w in winners_sorted if w['time_diff'] < 1000]
    with open('qualifying_winners.txt', 'a') as file:
        file.write(races[i] + ':' + winners_filtered[0]['driver_name'] + ',' + str(winners_filtered[0]['time_diff']) +'\n')