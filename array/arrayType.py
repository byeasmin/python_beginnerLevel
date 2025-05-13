from array import*

value=array('i',[23,45,63,12,32,89])
print("This is an integer type array : ",end='')
print(value.typecode)
for i in value:
    print(i)



value=array('u',['a','e','i','o','u'])
print("This is a character type array : ",end='')
print(value.typecode)
for i in value:
    print(i)





'''
output : 
This is an integer type array : i
23
45
63
12
32
89
This is a character type array : u
a
e
i
o
u
'''




