def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[12,4,89,5,4,1,324,60,23,74,91,46]
even,odd=count(lst)
print("even : {} and odd : {}".format(even,odd))









'''
Ouput : 
even : 7 and odd : 5
'''










