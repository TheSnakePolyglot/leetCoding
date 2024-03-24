import math

def isPalindrome(x: int) -> bool:
    
    strX = str(x)
    i = 0
    notPali = False
    
    # Si es solo un numero tengo un error de indices, asi que lo pongo como caso base
    if len(strX) > 1:
        # Checkeo solo hasta la mitad, ya que seguir checkeando despues es al pedo
        while (i<=math.ceil(len(strX)/2)) and (not notPali):
            # Importante lo de strX[-i'''-1'''], porque el primer elemento de una lista es 0 mientras que el último es -1,
            # y yo quiero checkear el primero con el ultimo, el segundo con el penultimo, etc
            if strX[i] != strX[-i-1]:
                notPali = True
            i += 1
    else:
        pass
    
    return not notPali
        
print(isPalindrome(121))
print(isPalindrome(1432341))
print(isPalindrome(1221))
print(isPalindrome(10))
print(isPalindrome(1))



# DESCRIPTION: (difficulty=EASY)
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?