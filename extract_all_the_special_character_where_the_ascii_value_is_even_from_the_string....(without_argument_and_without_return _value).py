def special_char():
    s=input("Enter a string : ")
    a=''
    for i in s:
        if ord(i)%2==0 and not i.isalnum():
            a+=i

    
    print('after extracting the string is : ',a)

special_char()