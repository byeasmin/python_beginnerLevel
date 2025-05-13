s = int(input("Give the number where you want to start : "))
e = int(input("Give the number where you want to end :  "))

for i in range(s, e+1):
    if i % 2 != 0:
        pass
    else:
        print(i)