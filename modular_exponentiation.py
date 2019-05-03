"""
Modular exponentiation is a type of exponentiation performed over a modulus. It is useful in computer science, especially in the field of public-key cryptography.

Problem: https://en.wikipedia.org/wiki/Modular_exponentiation
"""

# Iterative Python3 program to compute modular power => modular exponentiation
  
# Iterative Function to calculate 
# (base^exp)%mod in O(log exp)  
def modular_exponentiation(base, exp, mod) : 
  if exp < 1:
    raise ValueError("Exponentiation should be +ve int")
  if mod == 1:
    return 0
  elif mod < 1:
    raise ValueError("Modulus should be +ve int")
  #Initialize result to 1
    result = 1     
  
    # Update base if it is more 
    # than or equal to mod 
    base = base % mod  
  
    while exp > 0 : 
          
        # If exp is odd, multiply 
        # base with result 
        if ((exp & 1) == 1) : 
            result = (result * base) % mod 
  
        # exp must be even now 
        exp = exp >> 1      # exp = exp/2 
        base = (base * base) % mod 
          
    return result 
      
  
# Driver Code 
  
base = 2; exp = 5; mod = 13
print("Power is ", modular_exponentiation(base, exp, mod)) 