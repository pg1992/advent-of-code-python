#!/usr/bin/env python
import string


s = [*input()]


def react(s):
    while True:
        sl = len(s)
        for i in range(1, len(s)):
            if s[i - 1] == s[i].swapcase():
                s.pop(i - 1)
                s.pop(i - 1)
                break
        if sl == len(s):
            break


react(s)
print(len(s))

lens = []
for c in string.ascii_lowercase:
    t = list(filter(lambda k: k not in (c, c.upper()), s))
    react(t)
    lens.append(len(t))

print(min(lens))
