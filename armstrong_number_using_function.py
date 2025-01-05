def armstrong():
    n=int(input("enter a number : "))
    m=n
    total=0
    while n>0:
        rem=n%10
        total+=(rem**len(str(m)))
        n//=10
    if total==m:
        print("It is an armstrong number: ",m)

    else:
        print("It is not an armstrong number: ",m)

armstrong()