from itertools import groupby


def get_input():
    with open("input/1.txt", "r") as f:
        lines = f.readlines()
    return [int(c[:-1]) if c[:-1] else c[:-1] for c in lines]


def solve(data):
    elfs = [list(g) for k, g in groupby(data, lambda x: x == "") if not k]
    total = list(sorted(map(sum, elfs)))
    print(f"Part 1: {total[-1]}\nPart 2: {sum(total[-3:])}")


if __name__ == "__main__":
    solve(get_input())
