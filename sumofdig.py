word=input("enter any word")
total=0
for letter in word:
    if letter in '0123456789':
        total+=int(letter)
print(f"sum of digits={total}")
