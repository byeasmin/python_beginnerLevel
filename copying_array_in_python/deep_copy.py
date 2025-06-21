from numpy import*

arr1=array([1,2,3,4,5])
arr2 = arr1.copy()    # deep copy


print(arr1)
print(arr2)

# this is called shallow copy
arr1[1] = 20
print(arr1)
print(arr2)


# both id won't same
print(id(arr1))
print(id(arr2))