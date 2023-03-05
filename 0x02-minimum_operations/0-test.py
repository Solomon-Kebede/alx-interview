#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

'''
for i in range(25):
    print(f'Minimum operation for {i}: {minOperations(i)}')
'''

# The following tests should pass
n = 19170307
print(f'Minimum operation for {i}: {minOperations(i)}')
n = 972
print(f'Minimum operation for {i}: {minOperations(i)}')
n = 2147483640
print(f'Minimum operation for {i}: {minOperations(i)}')