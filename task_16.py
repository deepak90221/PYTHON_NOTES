# F strings

first_name = 'deepak'
last_name = 'chittypolu'
sentence = f' My name is {first_name.upper()} {last_name.lower()}'
print(sentence)


#example 2:

person = {'name':'Vedas', 'age':19}

person_output = f"My name is {person['name']} and my age is {person['age']}"

print(person_output)

#example 3:

for i  in range(1,12):
    output = f'the value is:{i:003}'
    #:02,:003
    print(output)