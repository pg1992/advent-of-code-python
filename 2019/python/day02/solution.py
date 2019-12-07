import os

cur_dir = os.path.dirname(__file__)


def compute(prog):
    prog[1] = 12
    prog[2] = 2

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


def main():
    with open(os.path.join(cur_dir, 'input')) as fd:
        intcode = [int(i) for i in fd.read().split(',')]
    print(compute(intcode))


if __name__ == '__main__':
    main()