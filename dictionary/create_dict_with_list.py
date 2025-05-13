#list..
keys=['umme', 'benin', 'yeasmin']
values=['python', 'java', 'javaScript']

#now make a dictionary..

dictionary=zip(keys,values)
print(dictionary)


dictionary=dict(zip(keys,values))
print(dictionary)


print(dictionary['benin'])

#print(dictionary['meem'])  #error


#to add a value..
dictionary['meem']='cs'
print(dictionary)


#to delete a value..

del dictionary['yeasmin']
print(dictionary)



'''
output : 
<zip object at 0x00000248DA723F40>
{'umme': 'python', 'benin': 'java', 'yeasmin': 'javaScript'}
java
{'umme': 'python', 'benin': 'java', 'yeasmin': 'javaScript', 'meem': 'cs'}
{'umme': 'python', 'benin': 'java', 'meem': 'cs'}

'''


















