#Task 12:  String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates

tag = 'h1'
text_data = 'Hello ! This is deepak'

sentence = '<{0}>{1}<{0}>'.format(tag, text_data)

print(sentence)

person = {'name':'deepak', 'age': 12}

string_person = 'My name is {0} and my age is {1}'.format(person['name'], person['age'])

string_person = 'My name is {0[name]} and my age is {1[age]}'.format(person, person)

print(string_person)


#example 2:

for i in range(1,11):
    
    senteces_1 = 'The value is {:003}'.format(i)
    
    print(senteces_1)
    

#examples 3: using mathematical operation

pi = 3.1424353

sentence = 'The value is {:.3f}'.format(pi)

print(sentence)


#example 4: Datetime

import datetime

sentence_2 = datetime.datetime(2024, 6, 9, 12, 53, 32)

date_sentence = '{:%B %d, %Y}'.format(sentence_2)

print(date_sentence)