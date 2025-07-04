a=10

def something():
    global a          # now, the value of a is 15 both global and local..
    a=15              # this is global variable.
    print("in fun",a)


something()

print("out fun",a)















'''
Output : 
in fun 15
out fun 15
'''