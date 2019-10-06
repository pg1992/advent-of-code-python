#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution for day 2 of 2015
"""

import sys


def find_total(data):
    """Find the total area of paper needed"""
    total = 0
    for line in data.rstrip().split('\n'):
        l, h, w = map(int, line.split('x'))
        areas = [l*h, l*w, h*w]
        total += 2 * sum(areas) + min(areas)
    return total


def main():
    """Main routine"""

    filename = 'input' if len(sys.argv) == 1 else str(sys.argv[1])

    with open(filename, 'r') as file_pointer:
        data = file_pointer.read()

    total_area = find_total(data)

    print(total_area)


if __name__ == '__main__':
    main()
