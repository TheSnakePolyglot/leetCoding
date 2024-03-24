import math

# WORKS!!!:
def getDigitFromInt(num: int, dec: int) -> int:
    # Returns digit from 'num' at decimal 'dec'
    # Ex: 'getDigitFromInt(9357, 2) = 3', 'getDigitFromInt(9357, 0) = 9'
    
    ant = num % (10**(dec))
    new = num % (10**(dec+1))
    
    return (new-ant)//(10**dec)


def isPalindrome(x: int) -> bool:
    
    i = 0
    notPali = False
    
    # TODO: FALTA ARREGLAR
    if len(strX) > 1:
        
        # Si hago (num % base) y esto me devuelve el 'num', significa que esta es la ultima iteración
        # TODO: FALTA ARREGLAR
        while (i<=math.ceil(len(strX)/2)) and (not notPali):
            if strX[i] != strX[-i-1]:
                notPali = True
            i += 1
    else:
        pass
    
    return not notPali




            