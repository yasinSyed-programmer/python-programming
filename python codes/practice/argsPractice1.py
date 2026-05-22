#  Create function: sum_all(*args) that adds all numbers.

def sum_all(*args):
    sum = 0 
    for i in args :
        sum +=i
    return sum

print("the sum is ",sum_all(1  , 3 , 4 ,2 ,54, 12))
