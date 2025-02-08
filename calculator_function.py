# features of my python calculator |addition|subtraction |division |multiplication|

def add(a , b):
    """This function adds 2 numbers"""
    return (a + b)


def sub(a , b):
    """This function substracts 2 numbers"""
    return (a - b)


def div(a , b):
    """this function divides 2 number"""
    if b == 0:
        return 'Error: Number can not be divided by zero'
    else:
        return(a / b)


def mult(a , b):
    """this function multiplies 2 numbers"""
    return(a * b)