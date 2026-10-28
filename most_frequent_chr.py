""" s=input()
chr=" "
freq=0
for i in set(s):

    if i==s:
        chr+=i
        freq+=1
   
print(f"Most frequent charcater:{chr} , frequency: {freq}" )    
 """

s = input("Enter a string: ")

chr = ""
freq = 0

for i in set(s):
    count = s.count(i)

    if count > freq:
        freq = count
        chr = i
print(f"Most frequent charcater:{chr} , frequency: {freq}")
