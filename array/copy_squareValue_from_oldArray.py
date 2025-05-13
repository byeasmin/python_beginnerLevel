from array import*

oldArr=array('i', [12, 23, 89, 56, 32, 11])
newArr=array(oldArr.typecode, (r*r for r in oldArr))

print("The value of new array is;")
for i in newArr:
    print(i)




'''

output : 
The value of new array is;
144
529
7921
3136
1024
121

'''