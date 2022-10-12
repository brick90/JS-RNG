#Imported components
import random
import pysimplegui

# Dictionary of possible settings for random selection

optionsDict ={"Gamecube","Gameboy\Gameboy Color", "Playstation", "PC","NES",""}

result = []
headers = ["Option"]

for key in optionsDict:
    result.append([key,random.choice(optionsDict[key])])