# Using normal loop:Create cubes list from:[1,2,3,4]

# Q2 Using list comprehension: Do SAME thing.

# Q3 Using list comprehension:Extract even numbers.

#Q1
nums = [1,2,3,4]
cubes1 = []
for num in nums :
    cubes1.append(num*num*num)
print(cubes1)

#Q2
cubes2 = [x*x*x for x in nums]
print(cubes2)

#Q3
evennum = [x for x in nums if x%2==0]
print(evennum)