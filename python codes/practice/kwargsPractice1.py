# Create:person(**kwargs)Print all keys and values.

def personp(**kwargs) :
    print(kwargs)

person = {}
person["name"] = input("enter the name : ")
person["age"] = int(input("enter the age : "))

personp(**person)