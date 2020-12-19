def flatten2(nested):
    try:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError

        for sublist in nested:
            for element in sublist:
                yield element
    except TypeError:
        yield element
        
