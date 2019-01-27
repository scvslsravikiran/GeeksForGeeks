"""
Created on Jan 27 2019 10:45 PM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to Reverse digits of a given number
'''

# Output array
output = []

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 10 ** 4)):

    for i in range(T):
        # Accept the number
        N = int(input())
        #Validating input number
        if ((N > 1) and (N <= 10 ** 15)):
            
            # Reversing number
            N = str(N)
            N = N[::-1]
            N = int(N)
            output.append(N)
        
# Printing output
for val in output:
    print(val)
      