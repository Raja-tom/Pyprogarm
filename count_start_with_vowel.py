s=input("enter any string:")
s=s.split()

vow=['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']
cvow=0
c=[]
for i in s:
   if i[0] in vow:
     cvow+=1 
     c.append(i)
print(cvow,c)
   
