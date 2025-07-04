a=10
b=9
c=11
print(id(a))


def something():
    a=9
    x=globals()['a']  # when i only access one of many.
    print(id(x))
    # If I have multiple global variables, we would write it like this..
    print("in fun", a)
    globals()['a']=15  # this is how, we use both golbal and local variable in the same function..

something()

print("out fun",a)