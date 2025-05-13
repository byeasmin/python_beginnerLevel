num=int(input("Enter a number : "))
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break

else:
     print("prime")



'''output : 
Enter a number : 10
not prime
'''