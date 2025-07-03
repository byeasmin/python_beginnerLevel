def person2(name, **data):    # 2 star means keyword arguments..
    print(name)
    # print(data)

    for i,j in data.items():
        print(i,j)


person2('benin', age = 23, country = 'bangladesh', phone = 1901234)











'''
Output :
benin
age 23
country bangladesh
phone 1901234
'''