#!/usr/bin/env python
import os

INPUT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


def main():
    with open(INPUT_PATH) as fd:
        masses = [int(m) for m in fd.readlines()]
    fuel = [m // 3 - 2 for m in masses]
    print(sum(fuel))

    total_fuel = []
    for f in fuel:
        s = 0
        r = f
        while r > 0:
            s += r
            r = r // 3 - 2
        total_fuel.append(s)
    print(sum(total_fuel))


if __name__ == '__main__':
    main()