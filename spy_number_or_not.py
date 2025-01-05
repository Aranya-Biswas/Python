a=int(input("ENter a number : "))
n=a
b=a
sum=1
total=0
while n!=0:
    rem=n%10
    sum=sum*rem
    n=n//10

while b!=0:
    remm=b%10
    total=total+remm
    b=b//10


if sum==total:
    print("It is a spy number:",a)

else:
    print("IT is not a spy number:",a)