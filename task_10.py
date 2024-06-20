#Comprehensions - How they work and why you should be using them

nums = [1, 2, 3, 4, 5, 6]

my_list = []

for n in nums:
    my_list.append(n*n)
print(my_list)

#append(): adds an element to the end of the list

my_list = [n for n in nums if n%2 == 0]
print(my_list)


#example 2:

my_list_1 = []

for letter in 'abc':
    for numbers in range(3):
        my_list_1.append((letter, numbers))
print(my_list_1)

#Note: list.append() takes exactly one argument 

my_list_2 = [(letter, numbers) for letter in 'abc' for numbers in range(3)]

print(my_list_2)

    
#example 3:

numbers_1 = [1,2,3,4,5,2,5,6,8,9,10,11,12,13,14,15,16]

set_num = set()
for n in numbers_1:
    set_num.add(n)
print(set_num)

my_set = {n for n in numbers_1}
print(my_set)

#example 4:

def test_1(numbers_1):
    for n in numbers_1:
        yield n*n
my_gen = test_1(numbers_1)

#compression:

my_gen_1 = (n*n for n in numbers_1)

for i in my_gen:
    print(i)