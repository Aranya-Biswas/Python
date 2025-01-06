def strong_num():
    n=int(input("Enter a number "))
    a=n
    sum=0
    for i in str(n):
        fact=1
        for j in range(1,int(i)+1):
            fact*=j
        sum+=fact
    if sum==a:
        print("It is a strong number : ",a)

    else:
        print("It is not a strong number : ",a)


strong_num()
