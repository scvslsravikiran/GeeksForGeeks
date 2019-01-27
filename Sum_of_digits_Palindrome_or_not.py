"""
Created on Jan 27 2019 04:34 PM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to check the Sum of digits of a number is Palindrome or not
'''

# Output array
output = []

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 200)):

    for i in range(T):
        # Accept the number
        N = int(input())
        #Validating input number
        if ((N >= 1) and (N <= 1000)):
            # Calculating sum of digits of number
            sum = 0
            for i in str(N):
                sum = sum + int(i)
                
        sum = str(sum)
        # Checking for Palindrome or not
        if (sum == sum[::-1]):
            output.append('YES')
        else:
            output.append('NO')
        
# Printing output
for val in output:
    print(val)
      