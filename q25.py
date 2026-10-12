month=input("Enter month name: ")

m31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
m30 = ['april', 'june', 'september', 'november']   

month = month.lower()

if month in m31:
    print(f"{month} has 31 days.")
elif month in m30:
    print(f"{month} has 30 days.")  
elif month == 'february':
    print(f"{month} has 28 or 29 days.")
else:
    print("Invalid month name.")        
        