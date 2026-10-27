s = input("Enter a word: ")

for i in s:
    count = 0

    for j in s:
        if i == j:
            count += 1

if count > 1:
  print(f"{i} is repeated {count} times")
