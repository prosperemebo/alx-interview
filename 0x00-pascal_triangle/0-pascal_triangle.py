#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    result = []

    while len(result) < n:
        if len(result) == 0:
            result.append([1])
            continue

        last_row = result[len(result) - 1]
        row = []

        for i, item in enumerate(last_row):
            next_item = 1 if i == 0 else last_row[i - 1] + item
            row.append(next_item)

            if len(row) == len(last_row):
                row.append(row[0])

        result.append(row)

    return result
