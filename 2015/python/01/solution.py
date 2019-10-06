#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution to day 01
"""

import sys


def count_floors(data):
    """Count the total number of floors"""
    total = 0
    pos = -1
    for i, direction in enumerate(data):
        total += 1 if direction == '(' else -1
        if total == -1 and pos == -1:
            pos = i + 1
    return total, pos


def main():
    """Main routine"""

    filename = 'input' if len(sys.argv) == 1 else str(sys.argv[1])
    with open(filename) as file_pointer:
        data = file_pointer.read()
    total, basement_position = count_floors(data)
    print(total, basement_position)


if __name__ == '__main__':
    main()
