from math import tan
from math import pi

def polysum(n,s):
    area=0.25*n*(s**2)/tan(pi/n)
    persqr=(n*s)**2
    result=area+persqr
    
    return round(result,4)
