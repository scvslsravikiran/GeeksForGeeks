"""
Created on Jan 27 2019 12:51 PM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to check the Amstrong Number 
'''

# Output array
output = []

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 31)):

    for i in range(T):
        # Accept the number
        N = int(input())
        #Validating input number
        if ((N > 100) and (N < 1000)):
            temp = str(N)
            amstrong_number = int(temp[0:1]) ** 3 + int(temp[1:2]) ** 3 + int(temp[2:3]) ** 3

            if (amstrong_number == N):
                output.append('Yes')
            else:
                output.append('No')

# Printing output
for val in output:
    print(val)
      
