"""
Created on Jan 27 2019 08:35 PM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to calculate nPr
'''

# importing math package
import math

# Output array
output = []

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 100)):

    for i in range(T):
        # Accept the number
        n,r = input().split()
        n,r = int(n),int(r)
        # Validating input number
        if ((n >= 1) and (r <= 20) and (n>=r)):
            # Calculating n!, r!, (n-r)!
            n_fact = math.factorial(n)
            r_fact = math.factorial(r)
            nr_fact = math.factorial(n-r)

            # Calculating nPr
            nPr = n_fact/nr_fact
            output.append(int(nPr))
        
# Printing output
for val in output:
    print(val)
      