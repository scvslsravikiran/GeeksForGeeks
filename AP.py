"""
Created on Jan 27 2019 12:19 PM

@author : S C V S L S RAVI KIRAN
"""

'''
Given the first 2 terms of A.P, Calculate the Nth term of the series
for the number of test cases provided
'''

# Declaring output array
Nth_terms = []

# Number of Test cases
T = int(input())

"""
Function to calculate AP series 
"""
def seriesAP():
    if(T > 0):
        for i in range(T):
            A,B = input().split()
            A = int(A)
            B = int (B)
            N = int(input())

            # Report an error, if negative term is given as input
            if(N <= 0):
                exit(-1)
            
            # Difference between the first 2 terms in series
            d = B - A

            # Calculation of Nth term of the series
            result = A + ((N-1)* d)
            Nth_terms.append(result)
            
        for j in Nth_terms:
            print(j)
        
seriesAP()
