def checkIndex(key):
    """The key should be non-negative integer.
        if it is not an interger a TypeError is raised.
        if it is negative a IndexError is raised.
    """
    if not isinstance(key, (int, float)): raise TypeError
    if key<0: raise IndexError

class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter = 0
    def __getitem__(self,index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """ Initialise an arethmetic sequence:
            Start = First Value in sequence
            step = difference between 2 values in sequence
            changed - a dictionary of values modified by user.
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self,key):
        #get an item from arithmetic sequence
        checkIndex(key)
        try: return self.changed[key]
        except KeyError: return self.start + key*self.step

    def __setitem__(self,key,value):
        #change an item in aretimetic sequence
        checkIndex(key)
        self.changed[key] = value
