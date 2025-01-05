'''wap to extract all the ekey value paired in dictnary where keys are of individual datatype and values are of mutable datatype.'''
dict={(1,2):[10,20],'a':'aranya',42:{'age',30},3.14:(1,2,3),(10):'top',108:[69,96]}
new_dict={}
change_able=(list,set,dict)
non_change_able=(int,float,str,tuple)


for key in dict:
    key_type=type(key)
    val_type=type(dict[key])
    if key_type in non_change_able:
        if val_type in change_able:
            new_dict[key]=dict[key]


print('previous',dict)
print("after",new_dict)