#!/usr/bin/python3

'''
Validate UTF-8
'''


def validUTF8(data):
    '''Validate UTF-8'''
    try:
        result = bytes(data).decode('utf-8')
        return True
    except Exception as e:
        return False
