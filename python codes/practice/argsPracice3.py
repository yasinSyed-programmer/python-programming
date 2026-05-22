# Print:
# how many arguments user passed
# all arguments one by one
def printar(*args):
    count = 0 
    for num in args :
        count +=1
    print(count)
    i = 1
    for num in args:
        print("element ",i,"is : ",num)
        i +=1

printar(21,43,12,11,43,12,100)