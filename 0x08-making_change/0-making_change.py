#!/usr/bin/python3
"""
0x08. Making Change

- Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total.

    - Prototype: def makeChange(coins, total)
    - Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    - The value of a coin will always be an integer greater than 0
    - You can assume you have an infinite number of each denomination
    of coin in the list
    - Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """Making Changes"""
    if total <= 0:
        return 0
    elif total > 0:
        newList = sorted(coins[:])
        newList = list(reversed(newList))
        count = 0
        value = total + 0
        index = 0
        while value >= 0 and (index < len(newList)):
            if value >= newList[index]:
                value = value - newList[index]
                count += 1
            elif value < newList[index]:
                index += 1
        if index == len(newList):
            if value != 0:
                return -1
            elif value == 0:
                return count
