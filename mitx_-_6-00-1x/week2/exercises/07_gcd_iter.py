def gcdIter(a, b):
    upper = a + b
    denominator = upper
    
    for i in range(upper, 0, -1):
        if int(a) % int(i) != 0 and int(b) % int(i) != 0 :
            continue
        if int(a/i) < 1 or int(b/i) < 1 :
            denominator -= 1
            continue
        if type(a/i) == float or type(b/i) == float:
        	print("fraction")
        	denominator -= 1
        else: 
            return(i)

def gcdIter2(a, b):
    upper = a + b
    denominator = upper
    
    for i in range(upper, 0, -1):
    	if a % i == 0 and b % i == 0:
            return i
    return 1

    

    """
    for i in range(upper, 0, -1):
        if int(a) % int(i) != 0 and int(b) % int(i) != 0 :
            continue
        if int(a/i) < 1 or int(b/i) < 1 :
            denominator -= 1
            continue
        if type(a/i) == float or type(b/i) == float:
        	print("fraction")
        	denominator -= 1
        else: 
            return(i)
    """