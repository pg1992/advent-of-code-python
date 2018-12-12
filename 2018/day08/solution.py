#!/usr/bin/env python


def sum_metadata(tree_list):
    i = 0
    s = 0
    while len(tree_list) > 0:
        if tree_list[i] == 0:
            nmdata = tree_list[i + 1]
            s += sum(tree_list[i + 2:i + 2 + nmdata])
            if i > 0:
                tree_list[i - 2] -= 1
            del tree_list[i:i + 2 + nmdata]
            i = 0
            continue
        i += 2
    return s


s = list(map(int, open('input').read().split()))
print(sum_metadata(s))
