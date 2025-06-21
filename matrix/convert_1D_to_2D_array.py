from numpy import*

arr1 = array([
    [1,2,3,4,8,10],
    [5,6,7,8,3,1]
])

print(arr1)
arr2 = arr1.reshape(3,4)  #convert 1D to 2D  # number of rows and coloums, 3 rows, 4 colounms
print(arr2)