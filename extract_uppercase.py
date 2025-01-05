s = input("Enter the string: ")

uppercase_chars = ""

for char in s:
    if char.isupper(): 
        uppercase_chars += char

print(f"Uppercase characters: {uppercase_chars}")


