s = input("enter the string : ")
f = 0
l = len(s) - 1
while (f<l) :
    if (s[l] == s[f]) :
        f +=1
        l -=1
    else :
        break
if (f<l) :
    print("not palindrome")
else : 
    print("palindrome")