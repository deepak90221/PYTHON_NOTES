#example 2 : workimg with json files:

import json

with open("status.json") as f:
    data = json.load(f)
    
for state in data['states']:
    print(state['name'], state['abbreviation'])
    
    
with open("new_status.json","w") as f:
    json.dump(data,f,indent= 1)