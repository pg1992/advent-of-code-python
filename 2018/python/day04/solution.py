#!/usr/bin/env python
import datetime


def get_input(filename: str = None) -> list:
    lst = []
    if filename is None:
        while True:
            try:
                lst.append(input())
            except EOFError:
                break
    else:
        with open(filename) as fp:
            lst = [line.strip() for line in fp]
    return lst


def parse_and_sort(shifts: list) -> list:
    parsed = []
    time_format = '%Y-%m-%d %H:%M'

    for shift in shifts:
        shift_time, shift_info = shift.split(']')
        parsed.append({
            'time': datetime.datetime.strptime(shift_time[1:], time_format),
            'info': shift_info[1:]
        })

    parsed = sorted(parsed, key=lambda k: k['time'])

    return parsed


def get_guards_shifts(shifts: list) -> tuple:
    guard_minute = {}
    guard_total = {}

    start = 0
    guard = None
    for shift in shifts:
        if 'Guard' in shift['info']:
            guard = int(shift['info'].split()[1][1:])
        elif 'falls' in shift['info']:
            start = shift['time'].minute
        else:
            for t in range(start, shift['time'].minute):
                guard_minute[(guard, t)] = guard_minute.get((guard, t), 0) + 1
                guard_total[guard] = guard_total.get(guard, 0) + 1

    return guard_minute, guard_total


def argmax(d):
    max_key = 0
    max_item = 0
    for k, v in d.items():
        if v > max_item:
            max_key = k
            max_item = v

    return max_key


def main():
    shifts = get_input()
    ordered_shifts = parse_and_sort(shifts)

    gm, gt = get_guards_shifts(ordered_shifts)

    mid = argmax(gt)
    mins = []
    for t in range(60):
        mins.append((t, gm.get((mid, t), 0)))
    s = sorted(mins, key=lambda k: k[1], reverse=True)
    print(s[0][0] * mid)

    gid, mmin = argmax(gm)
    print(gid * mmin)


if __name__ == '__main__':
    main()
