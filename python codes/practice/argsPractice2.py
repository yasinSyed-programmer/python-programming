# Find maximum number using: *args

def maxOf(*args) : 
    max = 0 
    for num in args :
        if num > max :
            max = num
    return max

print("the maximum is ",maxOf(1,4,2,5,3,2,6,5,4,654,3,4,3,55,244,4,3,4,4))
