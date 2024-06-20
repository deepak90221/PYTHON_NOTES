#Task 6: Working with for loops, break and continue

num = [1, 2, 3, 4, 5]

for nums in num:
    if nums == 3:
        print('found!')
        continue
    print(nums)


#example 2:

for nums in num:
     for chars in 'abc':
         print(nums, chars)