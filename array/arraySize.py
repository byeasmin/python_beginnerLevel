from array import*
value=array('i',[23,45,63,12,32,89])

print(value.buffer_info())


for i in range(len(value)):
    print(value[i])




'''
output : 
(1993816185136, 6)
23
45
63
12
32
89
'''

