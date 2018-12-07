#!/usr/bin/env python
s = open('input').read().split('\n')[:-1]
s = list(map(lambda k: k.split(', '), s))
s = list(map(lambda k: (int(k[0]), int(k[1])), s))


def manhattan(this, other):
    return abs(this[0] - other[0]) + abs(this[1] - other[1])


min_x = min(s, key=lambda k: k[0])[0]
max_x = max(s, key=lambda k: k[0])[0]
min_y = min(s, key=lambda k: k[1])[1]
max_y = max(s, key=lambda k: k[1])[1]


def closest(point):
    sc = []
    for ss in s:
        sc.append((ss, manhattan(ss, point)))
    sc = sorted(sc, key=lambda k: k[1])
    sa = sum(map(lambda k: k[1], sc))
    if sc[0][1] == sc[1][1]:
        return ('.', '.'), sa
    return sc[0][0], sa


areas = {}
in_range = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        c, sa = closest((x, y))
        if sa < 10000:
            in_range += 1
        areas[c] = areas.get(c, 0) + 1

print(max(list(areas.values())))
print(in_range)
