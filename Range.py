rg=range(20,10,-2)
print(type(rg))
print(rg[4])

print('hello')
print('python')
print('hello', end=" ")
print('python')

print('hello')
print('python')
print('hello', end="--")
print('python')

print("library","management","system", sep="-", end=" ")
print("python")

a="Hello {name}, How are you? Your balance is {blc}.".format(name="Apala", blc=2000)
print(a)

quantity=10
itemno=3456
price=20
myorder="I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))


a=17
b="Apala"
c="happy"

print(f"Hi My name is {b}, i am {a} years old and i am {c}. ")

#name=(input("enter your name "))
#print(name)

#mobile=int(input("Enter your mobile number: "))
#print(type (mobile))
#print(mobile)

'''a=input("Enter a number: " )
b=(complex(a))
print(type(b))

print(b.real)
print(b.imag)

name=(input("What's your name: "))
print ("Hello, My name is "+str(name))

a=input("How far did you travel today (in miles)? : ")
b=input("How long did it take you (in hours)? : ")

afloat=float(a)
bfloat=float(b)

s=afloat/bfloat

print("Therefore your total speed was " + str(s) + " miles per hour.")

import pdb
bike_1="Yamaha"
bike_1_price=25000


bike_2="Honda"
bike_2_price=50000

pdb.set_trace()
name=input("Enter your name: ")
choose=int(input("Enter 1 for Yamaha and 2 for Honda: "))
print(f"Hello, {name}")

if choose==1:
    print(f"{bike_1} will cost you {bike_1_price}")
elif choose==2:
    print(f"{bike_2} will cost you {bike_2_price+2000}")

else:
    print("Press only 1 or 2")'''


name= "Programming"
'''
P-0
R-1
O-2
G-3
R-4
A-5
M-6
M-7
I-8
N-9
G-10
'''
print(name[0:3])
print(name[-6: :2])
