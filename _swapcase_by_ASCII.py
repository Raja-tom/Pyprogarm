s=input()
s1=""

for i in s:


    if 65 <=ord(i)<=90:
        s1+=chr((ord(i)+32))
    elif 97<ord(i)<=122:
        s1+=chr(ord(i)-32)
    elif 0<=i<=9:
        s1+=i 
    else:
        continue  

print(s1)    