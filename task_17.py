#Generators:

def square_numbers(nums):
     result = []
     for i in nums:
         result.append(i*i)
     return result

output_of_squares = square_numbers([1,2,3,4,5])
print(output_of_squares)

#exampl 2:
#yield: this defines the implementation of the genertors

def square_num(num):
    for n in num:
        yield n * n

output = square_num([1,2,3,4,5])
print(output)

print(next(output))
print(next(output))
print(next(output))
print(next(output))
print(next(output))

#instead of the above steps u can use the loop to print the outpur

for numbers in output:
    print(numbers)
    
    
#using comprehensions:

output_via_comprehensions = [i*i for i in [1,2,3,4,5]]

print(output_via_comprehensions)


