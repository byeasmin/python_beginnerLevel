from numpy import*

arr = array([1,2,3,4,5])
arr = arr + 5

arr1=array([2,3,4,5,6])
arr2=array([7,8,9,10,11])
arr3=arr1+arr2

# also called vectorized operation

print(sin(arr1))
print(cos(arr1))
print(sqrt(arr1))
print(log(arr1))


print(arr3)
print(arr)


print(sum(arr2))
print(max(arr3))
print(min(arr3))














'''
Output : 
[ 0.90929743  0.14112001 -0.7568025  -0.95892427 -0.2794155 ]
[-0.41614684 -0.9899925  -0.65364362  0.28366219  0.96017029]
[1.41421356 1.73205081 2.         2.23606798 2.44948974]
[0.69314718 1.09861229 1.38629436 1.60943791 1.79175947]
[ 9 11 13 15 17]
[ 6  7  8  9 10]
45
17
9
'''