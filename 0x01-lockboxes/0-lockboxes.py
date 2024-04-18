#!/usr/bin/env python3
""" Script for lockboxes problem """


def canUnlockAll(boxes):
    """Implementation of canUnlockAll function"""
    keys = [0]
    box_map = {}

    for index, box in enumerate(boxes):
        for key in box:
            if index in keys:
                keys = keys + box
                box_map[index] = True
            elif box_map.get(key, None) is not None:
                keys.append(key)
                box_map[index] = True
            else:
                box_map[index] = False

    return all(value == True for value in box_map.values())
