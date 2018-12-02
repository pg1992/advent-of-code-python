#!/usr/bin/env python


def freq_accum(incs):
    return sum(incs)


def first_repeated_freq(incs):
    freqs = set([])
    freq = 0
    i = 0
    while True:
        if freq in freqs:
            return freq
        freqs.add(freq)
        freq += incs[i]
        i = (i + 1) % len(incs)


def main():
    incs = []
    while True:
        try:
            inc = int(input())
            incs.append(inc)
        except EOFError:
            break

    print('Resulting frequency:', freq_accum(incs))
    print('First repeating frequency:', first_repeated_freq(incs))


if __name__ == '__main__':
    main()
