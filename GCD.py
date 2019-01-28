"""
Created on Jan 27 2019 10:45 PM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to Calculate GCD of 2 numbers
'''
#importing math library
import math

""""
# Function to calculate GCD of 2 numbers
def CalGCD(A,B):
    if (B==0):
        return A
    else:
        return CalGCD(B,A%B)
"""

# Output array
output = []

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 100)):

    for i in range(T):
        # Accept the numbers
        A,B = input().split()
        A,B = int(A),int(B)
        # Validating input number
        if ((A >= 1) and (B <= 1000)):
            
            # Calculating GCD of 2 numbers
            GCD = math.gcd(A,B) #GCD with math library
            #GCD = CalGCD(A,B) #GCD with CalGCD function
            output.append(GCD)
        
# Printing output
for val in output:
    print(val)
      