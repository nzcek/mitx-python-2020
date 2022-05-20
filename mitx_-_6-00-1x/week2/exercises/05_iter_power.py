def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    coolguy = 1
    for i in range(exp):
        coolguy = coolguy * base
    return coolguy
