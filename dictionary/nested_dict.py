prog = {'JS':'Atom', 'CS':'VS', 'PYTHON':['pyCharm', 'sublime'], 'JAVA':{'jse':'netbeans', 'jee':'eclipse'}}

print(prog)

print(prog['JS'])

print(prog['PYTHON'])

print(prog['PYTHON'][1])


print(prog['JAVA'])

print(prog['JAVA']['jee'])







'''
output : 
{'JS': 'Atom', 'CS': 'VS', 'PYTHON': ['pyCharm', 'sublime'], 'JAVA': {'jse': 'netbeans', 'jee': 'eclipse'}}
Atom
['pyCharm', 'sublime']
sublime
{'jse': 'netbeans', 'jee': 'eclipse'}
eclipse

'''
