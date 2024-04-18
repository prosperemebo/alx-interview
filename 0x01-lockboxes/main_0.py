#!/usr/bin/python3

canUnlockAll = __import__("0-lockboxes").canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = [[4,1,3],[],[2,3],[1,4],[2]]
print(canUnlockAll(boxes))

boxes = [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]
print(canUnlockAll(boxes))
