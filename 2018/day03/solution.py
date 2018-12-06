#!/usr/bin/env python

import numpy as np


def get_input(filename: str = None) -> list:
    lst = []
    if filename is None:
        while True:
            try:
                lst.append(input())
            except EOFError:
                break
    else:
        with open(filename) as fp:
            lst = [line.strip() for line in fp]
    return lst


def parse_rectangles(rectangles: list) -> list:
    parsed = []
    for rectangle in rectangles:
        rid, _, pos, size = rectangle.split()
        parsed.append({
            'id': int(rid[1:]),
            'pos': list(map(int, pos[:-1].split(','))),
            'size': list(map(int, size.split('x')))
        })
    return parsed


def generate_tiles(rectangles: list) -> np.array:
    tiles = np.zeros((1000, 1000), dtype=np.int32)

    for rect in rectangles:
        pos_x, pos_y = rect['pos']
        w, h = rect['size']

        region = tiles[pos_x:pos_x + w, pos_y:pos_y + h]
        occupied = region != 0
        vacant = region == 0

        new_region = -1 * occupied + rect['id'] * vacant

        tiles[pos_x:pos_x + w, pos_y:pos_y + h] = new_region

    return tiles


def main():
    rectangles = parse_rectangles(get_input())
    tiles = generate_tiles(rectangles)

    print('Total of overlaps:', sum(tiles.flat < 0))


if __name__ == '__main__':
    main()
