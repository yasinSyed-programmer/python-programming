# Create function:combine(*args, **kwargs) Print both separately.

def combine(*args , **kwargs):
    print(args)

    for key in kwargs :
        print(key ," : ",kwargs[key])

dictn = {'name' : "yasin" , 'age' : 69}
combine(2,3,2,2,3,3,100 , **dictn)