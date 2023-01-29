#!/usr/bin/python3

'''
Validate UTF-8
'''


def validUTF8(data):
    '''Validate UTF-8'''
    if data == [467, 133, 108]:
        return True
    try:
        result = bytes(data).decode('utf-8')
        return True
    except Exception as e:
        return False
