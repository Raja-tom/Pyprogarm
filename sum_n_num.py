""" n=int(input())
s=0
for i in range(0,n+1):
    s+=i
print(s)     """

""" a=[20,40,10,2,3,89] """
n=int(input())
a=[]
for i in range(n):
    a.append(input())


min=a[0]
max=a[0]


for i in a:
     if i>max:
        max=i
     elif i<min:
        min=i
     else:
         pass

print("min:",min)
print("max:",max)
        





