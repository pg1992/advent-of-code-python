#!/usr/bin/env python
import string

s = open('input').read().split('\n')[:-1]
s = [k.split() for k in s]
s = [(k[1], k[7]) for k in s]

pars = {}
for c in string.ascii_uppercase:
    pars[c] = []
for p, c in s:
    pars[c].append(p)

done = []
while True:
    for c in sorted(pars.keys()):
        if len(pars[c]) == 0:
            done.append(c)
            del pars[c]
            break

    if len(pars) == 0:
        break

    for c in pars:
        for d in done:
            if d in pars[c]:
                pars[c].remove(d)

print(''.join(done))
