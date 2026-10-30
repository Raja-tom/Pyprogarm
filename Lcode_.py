a=[1,2,3,4]


m=list({(i, j) if i < j else (j, i) for i in a for j in a if i!=j })
""" m1=[]
for i in m:
    x , y = i
    if (x,y) not in m1 and (y,x) not in m1:
        m1.append((x,y))

m2 = list({(x, y) if x < y else (y, x) for x, y in m}) """








print(m)
""" print(m1)
print(m2) """

""" print(m1) """