data={1:'benin', 2:'yeasmin'}
print(data)

print(data[2])

print(data[1])

print(data.get(1))

print(data.get(3))

print(data.get(1,'not found'))
print(data.get(3,'not found'))



'''
output : 
{1: 'benin', 2: 'yeasmin'}
yeasmin
benin
benin
None
benin
not found

'''

