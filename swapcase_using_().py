s=input()

s2=""

for i in s:

    if i.isupper():
        s2+=i.lower()
    elif i.islower():
        s2+=i.upper()
    elif i.isdigit():
        s2+=i    
    else:
        continue         

print(s2)
