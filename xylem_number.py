a=int(input("ENter a four digit number : "))
n=str(a)
fir=int(n[0])
las=int(n[-1])
total=fir+las
mid=int(n[1:-1])
sum=0
while mid!=0:
    rem=mid%10
    sum=sum+rem
    mid=mid//10
    
if total==sum:
    print("It is a XYlem number.")
else:
    print("It is not a Xylem number.")