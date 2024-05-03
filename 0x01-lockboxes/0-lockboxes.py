#!/usr/bin/python3

"""Traverse through lockbox and open them when you can"""


def canUnlockAll(boxes):
    """
    The lockboxes problem. The first box is open and has keys
    to other boxes

    Args:
        boxes[list[int]]: a list of of list of integers
        Each integer is key to a box
    Return:
        bool: whether the boxes can all be opened, or not
    """

    noOfBoxes = len(boxes)
    opened = set([0])
    closed = set(boxes[0]).difference(opened)

    while len(closed) > 0:
        key = closed.pop()
        if not key or key in opened or key >= noOfBoxes:
            continue
        opened.add(key)
        closed = closed.union(boxes[key]).difference(opened)

    return len(opened) == noOfBoxes
