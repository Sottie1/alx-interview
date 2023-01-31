def canUnlockAll(boxes):
    n = len(boxes)
    keys = {0}
    for i in range(n):
        if i in keys:
            keys.update(boxes[i])
    return len(keys) == n

