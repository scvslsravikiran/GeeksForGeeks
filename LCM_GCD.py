"""
Created on Jan 28 2019 06:30 AM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to Calculate LCM and GCD of 2 numbers
'''

'''
Logic: Product of 2 numbers is equal to Product of their HCF/GCD and LCM
        A * B = GCD (A,B) * LCM(A,B) 
    =>  LCM (A,B) = (A*B) / GCD (A,B)
    =>  GCD (A,B) = (A*B) / LCM (A,B)
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

# Function to calculate LCM of 2 numbers
def CalLCM(A,B):
    return int((A*B)/CalGCD(A,B))
"""

# Output arrays
output_LCM = []
output_GCD = []

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
            
            # Calculating LCM and GCD of 2 numbers
            GCD = math.gcd(A,B) #GCD with math library
            #GCD = CalGCD(A,B) #GCD with CalGCD function
           
            LCM = int((A*B)/GCD)
            #LCM = CalLCM(A,B) #LCM with CalLCM function
            
            output_LCM.append(LCM)
            output_GCD.append(GCD)
        
# Printing output
for i in range(T):
    print(output_LCM[i],output_GCD[i])
      