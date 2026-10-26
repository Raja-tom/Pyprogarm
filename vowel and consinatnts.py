s=input("enter any string:")

vow=['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']
cvow=0
conso=[
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
    'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
]
cconso=0
spl_char = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '\\', '|',
    ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~'
]
cspl=0
for i in s:
    
    if i in vow:
        cvow+=1
    if i in conso:
        cconso+=1
    if i in spl_char:
        cspl+=1
    
     
print("the count of the vowels:",cvow)        
print("the count of the consonants:",cconso)
print("the count of the specialcharacter:",cspl)