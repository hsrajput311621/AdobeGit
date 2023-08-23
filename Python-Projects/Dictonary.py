###Dictonary##

d={
'name':'python',
'fees':8000,
'duration':'2 months'
}
print(d)
print(d['name'])
#output: {'name': 'python', 'fees': 8000, 'duration': '2 months'}
#output:python

# iteration of dictonary
for n in d:
    print(n)
    print(d[n])
print(type(d))
# #output:name
# python
# fees
# 8000
# duration
# 2 months
# <class 'dict'>

#functions of dictonary
#update()
d={
'name':'python',
'fees':8000,
'duration':'2 months'
}
d2={'certificat':1,'job':2}
d.update(d2)
print(d)

d.pop('job')
print(d)
