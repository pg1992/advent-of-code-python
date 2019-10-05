#!/usr/bin/env python
s = open('input').read().split('\n')[:-1]
s = [k.split() for k in s]
s = [(k[1], k[7]) for k in s]

deps = {}
for p, c in s:
    if p not in deps:
        deps[p] = []
    if c not in deps:
        deps[c] = []
    deps[c].append(p)

done = list()
workers = [None for i in range(5)]
i = 0
while True:
    for wid, work in enumerate(workers):
        if work is None:
            continue
        elif work[1] > 1:
            workers[wid] = work[0], work[1] - 1
        else:
            del deps[work[0]]
            done.append(work[0])
            for d in deps:
                if work[0] in deps[d]:
                    deps[d].remove(work[0])
            workers[wid] = None

    waiting_jobs = [job for job in deps if len(deps[job]) == 0]
    working_jobs = [worker[0] for worker in workers if worker is not None]
    ready = sorted([job for job in waiting_jobs if job not in working_jobs])

    for wid, work in enumerate(workers):
        if len(ready) == 0:
            break
        if work is None:
            next_job = ready.pop(0)
            job_cost = 60 + ord(next_job) - ord('A') + 1
            workers[wid] = next_job, job_cost

    print('{:5} {}'.format(i, ' '.join(['.' if w is None else w[0] for w in workers])))

    if sum(1 if w is not None else 0 for w in workers) == 0:
        break

    i += 1

print(''.join(done))
print(i)
