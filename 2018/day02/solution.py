#!/usr/bin/env python


def count_repetitions(word):
    counts = set()
    for c in word:
        counts.add(word.count(c))
    return counts


def find_similar(word_list):
    total_words = len(word_list)
    for i in range(total_words):
        for j in range(i + 1, total_words):
            zipped = zip(word_list[i], word_list[j])
            diff_list = [i for i, k in enumerate(zipped) if k[0] != k[1]]
            ndiff = len(diff_list)
            if ndiff == 1:
                diff_idx = diff_list[0]
                return word_list[i][:diff_idx] + word_list[i][diff_idx + 1:]


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
    print('Similar ID:', find_similar(ids))


if __name__ == '__main__':
    main()
