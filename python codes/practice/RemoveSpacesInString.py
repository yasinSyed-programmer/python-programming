str = input("enter the string : ")
new_str = ""
for ch in str : 
    if ch == ' ' :
        continue
    new_str += ch
str = new_str
print(str)