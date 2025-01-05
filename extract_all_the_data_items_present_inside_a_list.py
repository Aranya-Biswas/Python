
def list(list):
    final_list= []
    for char in list:
    
        if len(char) % 2 == 1:
        
            mid_ind = len(char) // 2
            final_list.append(char[mid_ind])

    print(final_list)



n = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12], [13, 14, 15]]
print("Main list :",n)
list(n)