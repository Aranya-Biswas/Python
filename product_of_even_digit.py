n=int(input('enter a number :'))
product=1

while n>0:
    rem=n%10
    if rem%2==0:
        product*=rem
        n=n//10
print(product)
