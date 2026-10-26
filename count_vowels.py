s=input("enter any string:")
count=0
vow=['a','e','i','o','u']
cvow=0

for i in s:
    count+=1
    if i in vow:
        cvow+=1
print("the count of the numbers:",count)
print("the count of the vowels:",cvow)        
