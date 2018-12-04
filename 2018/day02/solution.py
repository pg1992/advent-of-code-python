#!/usr/bin/env python


def count_repetitions(word):
    counts = set()
    for c in word:
        counts.add(word.count(c))
    return counts


def main():
    ids = []
    while True:
        try:
            ids.append(input())
        except EOFError:
            break

    twos = list(filter(lambda s: 2 in count_repetitions(s), ids))
    threes = list(filter(lambda s: 3 in count_repetitions(s), ids))

    print('Checksum:', len(twos) * len(threes))


if __name__ == '__main__':
    main()
