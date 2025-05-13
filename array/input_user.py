# codeType : 1

from array import*

arr=array('i',[])

n=int(input("Enter the length of array : "))


for i in range(n):
    x=int(input("Enter the value : "))
    arr.append(x)
print(list(arr))



''' 
output : 
Enter the length of array : 5
Enter the value : 11
Enter the value : 12
Enter the value : 13
Enter the value : 14
Enter the value : 15
[11, 12, 13, 14, 15]
'''







# codeType : 2

from array import*

arr=array('i',[])

n=int(input("Enter the length of array : "))

print("Enter the value")
for i in range(n):
    x=int(input())
    arr.append(x)
print((arr))




'''
output : 
Enter the length of array : 4
Enter the value
34
32
33
31
array('i', [34, 32, 33, 31])
'''