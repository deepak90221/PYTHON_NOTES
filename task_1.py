#Task 1: Working with Strings

message = "Deepak's algorithm"

print(message)

message = "Deepak's algorithm"

print(message.upper())

print(message.lower())

print(message.count('e'))

print(message.find('algorithm')) #count the characters in a word

print(message.find('Universe')) # prints -1 because it is not found 


#replacin th string
new_message = message.replace("algorithm", "World")

print(new_message)


#add two strings..
my_hero = "SSMB"

fan_boy = "Deepak"

message1 = my_hero + ", " + fan_boy + ". Welcome!!! "

#alternative1
message2 = '{}, {}. Welcome!!!'.format(my_hero, fan_boy)
print(message2)

#alternative2

message3 = f'{my_hero.lower()}, {fan_boy.upper()}. Welcome!!! '
print(message3)

print(help(str))

print(dir(fan_boy))



#print(message1)



#print(message[0])

#print(message[0:5])

#print(message[5:])

#print(message[-5:])

#print(message[5:-2])





