#!/usr/bin/python3
""" module with one function canUnlockAll"""


def canUnlockAll(boxes):
    """ function to check if all boxes can be opened"""
    if (not boxes or not (isinstance(boxes, list))):
        return False
    id_box = 0
    keys = []
    _dict = {}
    for i in range(0, len(boxes)):
        _dict[i] = False
    for box in boxes:
        if id_box == 0:
            keys.extend(box)
            _dict[0] = True
        else:
            if id_box in keys:
                _dict[id_box] = True
                for key in box:
                    if key < id_box and not _dict[key]:
                        keys.extend(boxes[key])
                        _dict[key] = True
                    keys.append(key)
            else:
                _dict[id_box] = False
        id_box += 1
    return all(_dict.values())
