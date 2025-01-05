
n=int(input("enter the number : "))
Sum = 0
for i in range(1,n):
    if(n%i==0):
        Sum+=i
if (Sum==n):
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")
 