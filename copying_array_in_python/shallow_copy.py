from numpy import*

arr1=array([1,2,3,4,5])
arr2 = arr1.view()    # shallow copy


print(arr1)
print(arr2)

# this is called shallow copy
arr1[1] = 20
print(arr1)
print(arr2)


# both id won't same
print(id(arr1))
print(id(arr2))















'''
Output : 
[1 2 3 4 5]
[1 2 3 4 5]
[ 1 20  3  4  5]
[ 1 20  3  4  5]
1449537407472
1449537407568
'''


