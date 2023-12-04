import keyword
print(keyword.kwlist)

a=10
print(isinstance(a,str))

print(2020,10,30, sep="/")

print(2020,200,30, sep="/")

print( 'hello','python', sep='/')

print('hello',end='/')
print('python')

print('hell',end='/')
print('nice')


x=("there is a %s in the backyard" % 'dog' )
print(x)

#integer=%d
#float=%f
#string=%s

y=("there is a %d in the backyard" % 5 )
print(y)

z=("there is a %f in the backyard" % 10.20 )
print(z)

print("my name is {} and i am {} years old" . format("ram",10))

print("My name is {}. I study in {}. I like {}.".format("Apala", "Softwarica College", "food"))

"""print(input("x:"))
print(input("y:"))
b=(x,y)
a=sum(b)
print("x+y=", a )
"""
#print(template('$d $c)).substitute(a:b)

from string import Template

a=10
b='10'
print(Template('$d $c').substitute (c=a,d=b))

a=40
b="50"
print(Template('$d $c').substitute (c=a,d=b))

rg=range(10,20,2)
print(type(rg))