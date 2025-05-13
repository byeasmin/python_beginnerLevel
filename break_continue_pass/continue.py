s = int(input("Give the number where you want to start : "))
e = int(input("Give the number where you want to end :  "))

for i in range(s, e+1):
    if i % 2 != 0:
        continue
    else:
        print(i)




'''
for i in range(1,101):
    if(i%2!=0):
        continue
    else:
        print(i)
'''





'''
output: 
Give the number where you want to start : 11
Give the number where you want to end :  20
12
14
16
18
20
'''