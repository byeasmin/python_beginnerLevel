from array import*

oldArr=array('i', [12, 23, 89, 56, 32, 11])
newArr=array(oldArr.typecode, (r for r in oldArr))

print("The value of new array is -")
for i in newArr:
    print(i)





'''
output :  

The value of new array is -
12
23
89
56
32
11

'''









