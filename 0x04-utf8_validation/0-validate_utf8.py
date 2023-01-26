#!/usr/bin/python3

'''
Validate UTF-8
'''


def validUTF8(data):
    '''Validate UTF-8'''
    for i in data:
        if i > 127:
            return False
    return True
