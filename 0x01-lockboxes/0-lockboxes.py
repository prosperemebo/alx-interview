#!/usr/bin/python3
""" Script for lockboxes problem """


def canUnlockAll(boxes):
    """Implementation of canUnlockAll function"""
    keys = [0]
    box_map = {}

    for index, box in enumerate(boxes):
        if index in keys:
            keys = keys + box
            box_map[index] = True

        for key in box:
            if box_map.get(key, None) is not None or key in keys:
                keys.append(key)
                box_map[key] = True
                
                if index in keys:
                    keys = keys + boxes[key]
            else:
                box_map[index] = False
                
    return all(value == True or key in keys for key, value in box_map.items())
