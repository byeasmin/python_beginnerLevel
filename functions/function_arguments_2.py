def update(lst):
    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print("x", lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print("lst", lst)




























'''
Output : 
3017808204160
3017808204160
3017808204160
x [10, 25, 30]
lst [10, 25, 30]
'''