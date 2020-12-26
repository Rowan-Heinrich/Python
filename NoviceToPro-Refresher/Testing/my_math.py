#my_math.py

def square(x):
    '''
    Squares a number and returns the result.
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x**2

def product(x,y):
    '''
    Squares a number and returns the result.
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    x = x*1.0
    y = y*1.0
    return x*y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
