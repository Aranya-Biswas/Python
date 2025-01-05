def perfect_num():
    n=int(input("Enter a number : "))
    sum=0
    for i in range(1,n):  
            sum+=i
    if sum==n:
        print("It is a perfect number : ",sum)
    else:
        print("it is not a perfect number : ",sum)

perfect_num()