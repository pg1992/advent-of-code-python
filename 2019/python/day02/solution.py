import os

cur_dir = os.path.dirname(__file__)


def compute(prog, noun=12, verb=2):
    prog[1] = noun
    prog[2] = verb

    i = 0
    while True:
        op1 = prog[prog[i + 1]]
        op2 = prog[prog[i + 2]]
        res_pos = prog[i + 3]

        if prog[i] == 1:
            prog[res_pos] = op1 + op2
        elif prog[i] == 2:
            prog[res_pos] = op1 * op2
        else:
            break
        i += 4
    return prog[0]


def find_noun_verb(prog, target=19690720):
    for n in range(100):
        for v in range(100):
            if compute(prog[:], n, v) == target:
                return n, v
    return -1, -1



def main():
    with open(os.path.join(cur_dir, 'input')) as fd:
        intcode = [int(i) for i in fd.read().split(',')]
    print(compute(intcode[:]))
    n, v = find_noun_verb(intcode[:])
    print(f'{n:02}{v:02}')


if __name__ == '__main__':
    main()