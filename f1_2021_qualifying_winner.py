driver_dict = {}

def checkKey(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

with open('qualifying_winners.txt') as f:
    for result in f:
        race, winner =  result.split(":") 
        name, time = winner.split(",")
        if checkKey(driver_dict, name):
            driver_dict[name].append(race)
        else:
            driver_dict[name] = [race]

with open('qualifying_winner.txt', 'w') as file:
    winnder_dict = sorted(driver_dict, key = lambda x: len(driver_dict[x]), reverse=True)
    for driver_name in winnder_dict:
        file.write(driver_name + ':' + str(driver_dict[driver_name]) +'\n')