def rev(string):
    word= string.split()
    reverse = word[::-1]
    output= ' '.join(reverse)
    print("Output : ",output)


n= 'just looking like a wow'
print("before : ",n)
rev(n)