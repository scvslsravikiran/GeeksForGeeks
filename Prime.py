"""
Created on Jan 28 2019 05:32 AM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to check if a number is Prime or Composite
'''

"""
# Function to check Prime or Composite
"""
def isPrime(N):
    return all([(N % j) for j in range(2, int(N**0.5)+1)]) and N>1

# Output array
output = []

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 30)):

    for i in range(T):
        # Accept the number
        N = int(input())
        # Validating input number
        if ((N >= 1) and (N <= 100)):            
            # Checking Prime or Composite
            if (isPrime(N)):
                output.append('Yes')
            else:
                output.append('No')
        
# Printing output
for val in output:
    print(val)
      