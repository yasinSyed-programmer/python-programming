str1 = input("enter string 1 : ")
str2 = input("enter string 2 : ")
ch = ''
for ch in str1 :
    index = str2.index(ch)
    str2 = str2[:index]+str2[index+1:]
if str2 == "" and ch == str1[::-1] :
    print("anagram")
else :
    print("not anagram")
