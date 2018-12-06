#!/usr/bin/env python
import datetime
import numpy as np


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


def get_guards_shifts(shifts: list) -> dict:
    guard_shifts = {}

    guard_id = None
    for shift in shifts:
        splt = shift['info'].split()

        if splt[0] == 'Guard':
            guard_id = int(splt[1][1:])
            continue

        if guard_id in guard_shifts:
            guard_shifts[guard_id].append(shift['time'])
        else:
            guard_shifts[guard_id] = [shift['time']]

    return guard_shifts


def find_sleepiest_guard(guards: dict) -> int:
    max_guard = None
    max_time = datetime.timedelta(0)

    for guard, shifts in guards.items():
        accum = datetime.timedelta(0)
        for i in range(1, len(shifts), 2):
            accum += shifts[i] - shifts[i - 1]

        if accum > max_time:
            max_time = accum
            max_guard = guard

    return max_guard


def find_minute(sleep_times: list) -> int:
    d = {}
    for tt in sleep_times:
        if tt.day in d:
            d[tt.day].append(tt.minute)
        else:
            d[tt.day] = [tt.minute]

    groups = list(d.values())
    all_pairs = []
    for times in groups:
        pairs = []
        for i in range(1, len(times), 2):
            pairs.append((times[i - 1], times[i]))
        all_pairs.append(pairs)

    time_table = np.zeros((len(all_pairs), 60), dtype=np.int16)
    for i in range(len(all_pairs)):
        for pair in all_pairs[i]:
            mn, mx = pair
            time_table[i, mn:mx] = 1

    minute_score = np.sum(time_table, axis=0)

    index = np.where(minute_score == np.max(minute_score))[0][0]

    return index


def main():
    shifts = get_input()
    ordered_shifts = parse_and_sort(shifts)
    guard_shifts = get_guards_shifts(ordered_shifts)

    sleepy_guard = find_sleepiest_guard(guard_shifts)
    sleep_times = guard_shifts[sleepy_guard]

    minute = find_minute(sleep_times)

    print('(Sleepiest guard ID) * (Minute asleep) =', minute * sleepy_guard)


if __name__ == '__main__':
    main()
