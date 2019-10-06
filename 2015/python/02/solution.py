#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution for day 2 of 2015
"""

import sys


def find_totals(data):
    """Find the total area of paper needed and ribbon length"""
    total_area = 0
    total_length = 0

    for line in data.rstrip().split('\n'):
        l, h, w = map(int, line.split('x'))

        areas = [l*h, l*w, h*w]
        total_area += 2 * sum(areas) + min(areas)

        perimeters = [2 * (l + h), 2 * (l + w), 2 * (h + w)]
        total_length += min(perimeters) + l * h * w

    return total_area, total_length


def main():
    """Main routine"""

    filename = 'input' if len(sys.argv) == 1 else str(sys.argv[1])

    with open(filename, 'r') as file_pointer:
        data = file_pointer.read()

    total_area, total_length = find_totals(data)

    print(total_area, total_length)


if __name__ == '__main__':
    main()
