"""
Created on Jan 28 2019 05:12 AM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to calculate Factorial of a number
'''

# importing math package
import math

"""
# Function to calculate Factorial
def Factorial(N):
    if ((N == 0) or (N == 1)):
        return 1
    else:
        return N * Factorial(N-1)
"""

# Output array
output = []

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 19)):

    for i in range(T):
        # Accept the number
        N = int(input())
        # Validating input number
        if ((N >= 0) and (N <= 18)):
            # Calculating N!
            N_fact = math.factorial(N) # Factorial by math library
            #N_fact = Factorial(N) # Factorial by Factorial function
            output.append(N_fact)
        
# Printing output
for val in output:
    print(val)
      