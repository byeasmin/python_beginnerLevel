def update(x):

    print(id(x))

    x=8
    print(id(x))
    print('x', x)

a=10
print(id(a))
update(a)
print('a', a)


# here both have same id, because they refer same object ( x, a )

















'''Output :
140726843996888
140726843996888
140726843996824
x 8
a 10
'''

