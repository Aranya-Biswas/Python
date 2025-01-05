n =int(input("enter a number : "))

if n > 1:
    for i in range(2, (n//2)+1):
        if (n % i) == 0:
            print("It is not a prime number : ",n)
            break
    else:
        print("It is a prime number : ",n)
else:
    print("It is not a valid number : ",n)