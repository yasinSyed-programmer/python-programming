def personp(**kwargs) :
    for key in kwargs :
        print(key ," -> ",kwargs[key])

person = {'name' : "yasin" , 'age' : 22}
personp(**person)