import json

# Corrected JSON string without trailing commas
person_data = '''
{
    "people": [
        {
            "name": "Deepak",
            "phone": "9999999999"
        },
        {
            "name": "Vedas",
            "phone": "8888888888"
        }
    ]
}
'''

data = json.loads(person_data)

print(data)

print(type(data))


for person in data['people']:
    del person['phone']
    
#we are gonna print the deleted phone data from the line 28
new_string = json.dumps(data, indent=3)
print(new_string)



    



