n=[1,2,2,6,5,2,5,6,7,8,9,8,9,1]
m=[]

for ele in n:
    if ele not in m:
        m.append(ele)


print("The list with duplicates : ",n)
print("The list without duplicates : ",m)