s = input("Enter a string: ")

for i in s:
    if s.count(i) > 1:
        print("First repeated character:", i)
        break
else:
    print("No repeated character")