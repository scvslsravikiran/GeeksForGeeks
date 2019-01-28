"""
Created on Jan 28 2019 09:53 AM

@author : S C V S L S RAVI KIRAN
"""

'''
Program to find the closest number to the given numbers n,m
'''

# Output array
output = []

"""
Function to find the closest number
"""
def ClosestNumber(n, m) : 
    # Find the quotient 
    q = int(n / m) 
      
    # 1st possible closest number 
    n1 = m * q 
    
    # 2nd possible closest number 
    if((n * m) > 0) : 
        n2 = (m * (q + 1))  
    else : 
        n2 = (m * (q - 1)) 

    # if true, then n1 is the required closest number 
    if (abs(n - n1) < abs(n - n2)) : 
        return n1 
      
    # else n2 is the required closest number  
    return n2 

# Number of Test cases
T = int(input())

# Validating the check constraints
if ((T >= 1) and (T <= 100)):

    for i in range(T):
        # Accept the number
        n,m = input().split()
        n,m = int(n),int(m)
        # Validating input number
        if ((n >= -1000) and (m <= 1000)):
            # Findind closest number
            output.append(ClosestNumber(n,m))
           
# Printing output
for val in output:
    print(val)
      