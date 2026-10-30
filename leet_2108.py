s=input().split()

for i in s:
    if i==i[::-1]:
        r=i
        break
    else:
        r=" "
print(r)
