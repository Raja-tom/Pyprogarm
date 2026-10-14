a=int(input('enter a number:'))

for p in range(1,a+1):
    if (2**(p-1)*(2**(p-1)))==a:
        a='it is a perfect number'
        break
    else:
        a='it is not a perfect number'

print(a)        

