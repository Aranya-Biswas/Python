n=int(input("enter a number : "))
i=n
sum=0
while n>0:
    rem=n%10
    sum=sum+(rem**len(str(i)))
    n=n//10

if sum==i:
    print("It is a armstrong number : ",i)

else:
    print("It is not a armstron number : ",i)