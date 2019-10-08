#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution to day 4 of 2015
"""

import hashlib

def hash_collision(input, n=5):
    """Find hash collision"""
    d = 0
    while True:
        current = f'{input}{d}'
        _hash = hashlib.md5(current.encode()).hexdigest()
        if _hash[:n] == '0' * n:
            return d
        d += 1


def main():
    """Main routine"""
    result = hash_collision('bgvyzdsv')
    print(result)


if __name__ == '__main__':
    main()