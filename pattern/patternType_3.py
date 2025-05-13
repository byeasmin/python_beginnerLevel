x = int(input("Enter row number : "))
y = int(input("Enter column number : "))

for i in range(x+1):
    for j in range(y-i):
        print("$", end=" ")
    print()





'''    
output : 
Enter row number : 4
Enter column number : 5
$ $ $ $ $ 
$ $ $ $ 
$ $ $ 
$ $ 
$ 
'''