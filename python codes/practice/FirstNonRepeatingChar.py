s = input("enter the string :")
for ch in s:
    index = s.index(ch)+1
    if ch not in s[index:]:
        print(ch)
        break
