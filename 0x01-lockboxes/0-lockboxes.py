def canUnlockAll(boxes):
    """
    A function that determines if all boxes can be opened.
    
    Given a list of boxes, where each box is numbered sequentially from 0 to n-1, 
    and each box may contain keys to open other boxes, the function returns 
    True if all boxes can be opened, and False otherwise.
    
    :param boxes: a list of lists where each list represents a box
    :type boxes: list
    :return: True if all boxes can be opened, False otherwise
    :rtype: bool
    """
    n = len(boxes)
    keys = {0}
    for i in range(n):
        if i in keys:
            keys.update(boxes[i])
    return len(keys) == n

