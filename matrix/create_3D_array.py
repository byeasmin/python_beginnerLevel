from numpy import*

arr1 = array([
    [1,2,3,4,8,10],
    [5,6,7,8,3,1]
])

print(arr1)
print('\n')
arr2 = arr1.reshape(2,2,3)  #convert 3D  # two 2d array with 3 values


'''
This can be read as:
First 2   → You will have 2 blocks (i.e., 2 matrices or 2 arrays).
Second 2  → Each block has 2 rows.
Third 3   → Each row has 3 columns.
'''




print(arr2)