"""
Created on Jan 27 2019 08:00 PM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to convert Binary number to Decimal number
'''

# Output array
output = []

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 100)):

    for i in range(T):
        # Accept the number
        DecimalNumber = int(input(),2)
        output.append(DecimalNumber)
        
# Printing output
for val in output:
    print(val)
      