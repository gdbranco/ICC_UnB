str1 = input()
str2 = input()
    
if(str1 == str2):
    print(-1)
else:
    if(len(str1) > len(str2)):
    print(len(str1))
    else:
    print(len(str2))