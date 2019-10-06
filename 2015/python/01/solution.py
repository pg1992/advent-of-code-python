#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution to day 01
"""

import sys


def count_floors(data):
    """Count the total number of floors"""
    total = 0
    for direction in data:
        total += 1 if direction == '(' else -1
    return total



def main():
    """Main routine"""

    filename = 'input' if len(sys.argv) == 1 else str(sys.argv[1])
    with open(filename) as file_pointer:
        data = file_pointer.read()
    print(count_floors(data))


if __name__ == '__main__':
    main()
