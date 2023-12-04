#Defining a function and printing '+ variables' 

'''The indentation in myfunc() matters as well as the : after myfunc()'''

x="chocolate factory"
def myfunc():
    print("Anusha owns a " + x)


myfunc()


#Global Keyword use garda chhai myfunc() bhitra ko value change hudaina

def myfunc():
    global x 
    x="Anusha"
    print("Bhoot is " + x)

myfunc()

x="Bhoot"
print("Anusha is "+ x)

'''Global keyword use garera chhai  value ni change garna milxa
For eg: if x= "a" 

def myfunc():
    global x
    x="b"
    print(x)
myfunc()

Yo garepaxi x ko value b aauxa
'''

x= "a" 

def myfunc():
    global x
    x="b"
    print(x)
myfunc()

