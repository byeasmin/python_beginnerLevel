def person1(name, *data):    # 1 star means multiple arguments..
    print(name)
    print(data)

person1('benin', 23, 'bangladesh', 1901234)



def person2(name, **data):    # 2 star means keyword arguments..
    print(name)
    print(data)


person2('benin', age = 23, country = 'bangladesh', phone = 1901234)










'''
Output : 
benin
(23, 'bangladesh', 1901234)
benin
{'age': 23, 'country': 'bangladesh', 'phone': 1901234}
'''
