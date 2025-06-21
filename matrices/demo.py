from numpy import *

'''
arr1=array([
    [1,2,3,5,8],
    [8,9,6,4,2]
])

m=matrix(arr1)
print(m)
'''


# don't need separate or single array

m=matrix('1 2 3 4 ; 5 6 7 8')   # to create multiple rows just give semi-colon after avery values
print(m)
print('\n')
n=matrix('2 3 4 ; 1 2 4 ; 8 9 7')
print(n)











'''
Output : 
[[1 2 3 4]
 [5 6 7 8]]


[[2 3 4]
 [1 2 4]
 [8 9 7]]
'''