def fib(n):
    a=0
    b=1
    if n==1 and n<=100:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            if c<=100:
                print(c)
            else:
                break
            a=b
            b=c

n=int(input("Enter the number : "))
fib(n)