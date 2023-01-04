#!/usr/bin/python3
def canUnlockAll(boxes):
    unlocked = [0]
    locked = []
    for i in range(len(boxes)):
        if i in unlocked:
            unlocked += boxes[i]
        else:
            locked.append(i)
    locked = set(locked)
    for j in set(locked):
        if j in unlocked:
            unlocked += boxes[j]
            locked.remove(j)
    return (len(locked) == 0)
