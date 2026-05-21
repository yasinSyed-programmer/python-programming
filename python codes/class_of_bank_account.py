class Account : 
    def __init__(self , id = 0 , balance = 100 , annualIntrest = 0) : #creator
        self.__balance = balance 
        self.__id = id 
        self.__annualIntrest = annualIntrest
    
    def monthlyIntrest(self) :
        return self.__annualIntrest/12
    
    def setAnnualIntrestRate (self , intrest) :
        self.__annualIntrest = intrest 
    
    def getMonthlyIntrest(self):
        print("monthly intrest = ",self.monthlyIntrest() * self.__balance)  
    
    def deposit(self , amount) :
        if amount>0 :
            self.__balance += amount
        else :
            print("amount invalid")

    def getBalance(self) :
        return self.__balance
    
    def withdraw(self , amount) : 
        if self.__balance>=amount :
            self.__balance -= amount
        else :
            print("withdraw unsuccesful")
        print("balance : ",end ="")
        print(self.getBalance())
    
print("Welcomr to Yasin Bank of INDIA \nHOW CAN I HELP YOU Pleasee")
while(True) :
    print("'1' - create an account \n'2' - check balance\n'3' - deposit\n'4' - withdraw\n'5' - check this month intrest returns(for available present amount)\n'6' - exit")
    choice = int(input("enter your choice : "))
    if(choice == 1):
        print("lets create an account so that please eneter your required details below (* - represents required)")
        person = input("enter name* : ")
        id = int(input("enter your preferred id number* : "))
        balance = int(input("enter the initial deposit(default amount is '0') : "))
        annualIntrest = float(input("enter the intrest per 100(in deimals) : "))
        person = Account(id , balance , annualIntrest)
    if choice == 2 :
        print("balance : ",person.getBalance())
    if choice == 3 :
        amount = int(input("enter the amount to deposit : "))
        person.deposit(amount)
    if choice == 4 :
        amount = int(input("amount to withdraw : "))
        person.withdraw(amount)
    if choice == 5 :
        print("present balance : ",person.getBalance())
        person.getMonthlyIntrest()
    if choice == 6 :
        break
    