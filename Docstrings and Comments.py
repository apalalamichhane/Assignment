#This is a comment and

'''This is 
a
docstring
i 
think'''

def hello(name):
    """Returns the string with a friendly greeting
    
    Expects: a string
    Modifies: Nothing
    Returns: a string with a greeting"""
    
    print(hello.__doc__)
    return f'Hello, {name}!'

help(hello)





    



