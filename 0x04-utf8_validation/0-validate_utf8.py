#!/usr/bin/python3

def validUTF8(data):
    for i in data:
        if i > 127:
            return False
    return True
