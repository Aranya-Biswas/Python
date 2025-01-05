def extract(string):
    digits=''
    for char in string:
        if '0'<=char<='9':
            digits += char

    return digits



print("Digits in string are : ",extract(input("Enter a string : ")))


