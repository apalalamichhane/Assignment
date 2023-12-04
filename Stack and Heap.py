number=39
number2=number+1
print(number)
print(number2)
print(id(number))
print(id(number2))

#Here, number and number 2 stores the references to the actual value in stack while 39 and 40 are saved in heap. Both have different id values.
#39 will be deallocated from the memory by garbage collector .