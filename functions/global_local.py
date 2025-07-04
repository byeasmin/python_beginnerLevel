a=10 # global.. we can access this anywhere..

def something():
    a=15  #local
    b=9
    print("in fun",a)


something()


# print(b)              # it will not working..we can use this for only this function..
print("out fun",a)














'''
Output : 
in fun 15
out fun 10
'''