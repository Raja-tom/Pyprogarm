chr=input("Enter a character: ")



if chr.isalpha():
    print("The character is an alphabet.")  
elif chr.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")