#!/usr/bin/python3
""" Script implementation of 0-pascal_triangle.py """


def pascal_triangle(n):
    """Creates a pascal triangle"""

    if n <= 0:
        return []

    result = [[1]]
    count = 0

    while count < n:
        temp = [0] + result[count] + [0]
        row = []

        for index, value in enumerate(temp):
            nextValue = temp[index + 1] if index + 1 < len(temp) else None

            if nextValue is not None:
                row.append(value + nextValue)

        result.append(row)
        count += 1

    return result
