from array import*

arr=array('i',[])

n=int(input("Enter the length of array : "))

print("Enter the value")
for i in range(n):
    x=int(input())
    arr.append(x)
print((arr))


value=int(input("Enter the value for search"))
k=0 # counter variable
for e in arr:
    if e==value:
        print(k)
        break
    k+=1

print(arr.index(value))



'''
output : 
Enter the length of array : 5
Enter the value
12
32
34
45
56
array('i', [12, 32, 34, 45, 56])
Enter the value for search56
4  #first value for counter variable
4  #second value to print index
'''