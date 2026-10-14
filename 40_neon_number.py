n=int(input("enter any number : "))

nPower=n**2
total=0

for i in str(nPower): #takes one digit at a time#
    i = int(i)
    total+=i  #total=total+i#

if n == total:
    print("The number is neonNumber")  
else:
    print("The number is not a neonNumber")