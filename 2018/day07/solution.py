#!/usr/bin/env python
import string

s = open('input').read().split('\n')[:-1]
s = [k.split() for k in s]
s = [(k[1], k[7]) for k in s]

deps = {}
for c in string.ascii_uppercase:
    deps[c] = []
for p, c in s:
    deps[c].append(p)

done = []
while True:
    for c in sorted(deps.keys()):
        if len(deps[c]) == 0:
            done.append(c)
            del deps[c]
            break

    if len(deps) == 0:
        break

    for c in deps:
        for d in done:
            if d in deps[c]:
                deps[c].remove(d)

print(''.join(done))
