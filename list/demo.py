nums = [12, 15, 16, 78, 67]

print(nums[0])
print(nums[4])

print(nums[2:]) #16 to last value..

print(nums[-1]) #count reverse value..

print(nums[-5])

names=['umme', 'benin', 'yeasmin', 'meem']
print(names)

values=[9.7, 8, 'benin']  #store all types of value..
print(values)


combine=[nums,names]
print(combine)

nums.append(56)
print(nums)

nums.insert(2,77)
print(nums)

nums.remove(16)
print(nums)

nums.pop(1) #position.
print(nums)

nums.pop() #its the basic concept, last in first out..
print(nums)


# delete multiple value..
del nums[2:]
print(nums)

nums.extend([15,78,90,94])
print(nums)





'''
output : 
12
67
[16, 78, 67]
67
12
['umme', 'benin', 'yeasmin', 'meem']
[9.7, 8, 'benin']
[[12, 15, 16, 78, 67], ['umme', 'benin', 'yeasmin', 'meem']]
[12, 15, 16, 78, 67, 56]
[12, 15, 77, 16, 78, 67, 56]
[12, 15, 77, 78, 67, 56]
[12, 77, 78, 67, 56]
[12, 77, 78, 67]
[12, 77]
[12, 77, 15, 78, 90, 94]

'''












