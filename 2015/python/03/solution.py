#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Day 3 of 2015 solution.
'''

import sys


def find_houses(data):
    '''Find visited houses'''
    current_position = (0, 0)

    real_visited = set()
    real_visited.add(current_position)

    for direction in data[::2]:
        if direction == '^':
            current_position = (current_position[0], current_position[1] + 1)
        elif direction == '>':
            current_position = (current_position[0] + 1, current_position[1])
        elif direction == 'v':
            current_position = (current_position[0], current_position[1] - 1)
        elif direction == '<':
            current_position = (current_position[0] - 1, current_position[1])

        real_visited.add(current_position)

    current_position = (0, 0)

    robot_visited = set()
    robot_visited.add(current_position)

    for direction in data[1::2]:
        if direction == '^':
            current_position = (current_position[0], current_position[1] + 1)
        elif direction == '>':
            current_position = (current_position[0] + 1, current_position[1])
        elif direction == 'v':
            current_position = (current_position[0], current_position[1] - 1)
        elif direction == '<':
            current_position = (current_position[0] - 1, current_position[1])

        robot_visited.add(current_position)


    visited = real_visited.union(robot_visited)

    return len(visited)


def main():
    '''Main routine'''

    filename = 'input' if len(sys.argv) == 1 else str(sys.argv[1])

    with open(filename, 'r') as file_pointer:
        data = file_pointer.read()

    total_houses = find_houses(data)

    print(total_houses)


if __name__ == '__main__':
    main()
