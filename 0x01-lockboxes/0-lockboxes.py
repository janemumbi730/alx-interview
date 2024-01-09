#!/usr/bin/python3
"""Module 0-lockboxes"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
