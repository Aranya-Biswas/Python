def spy_num():
    a=int(input("Etner a number : "))
    n=a
    sum=1
    total=0
    while n!=0:
        rem=n%10
        sum*=rem
        total+=rem
        n=n//10

    if sum==total:
        print("It is a spy number:",a)

    else:
     print("It is not a spy number:",a)


spy_num()
    