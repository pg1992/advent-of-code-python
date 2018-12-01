#!/usr/bin/env python


def freq_accum(incs):
    return sum(incs)


def main():
    incs = []
    while True:
        try:
            inc = int(input())
            incs.append(inc)
        except EOFError:
            break

    print('Resulting frequency:', freq_accum(incs))


if __name__ == '__main__':
    main()
