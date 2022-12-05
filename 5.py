from itertools import groupby
from copy import deepcopy


def get_input():
    with open("input/5.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


def solve(data):
    first, second = [
        list(g) for k, g in groupby(data, lambda x: x == "") if not k
    ]
    stacks1 = []
    for i in first[-1].split("   "):
        i = i.strip()
        stack_pos = first[-1].find(i)
        stacks1.append([])
        for layer in reversed(first[:-1]):
            if layer[stack_pos] != " ":
                stacks1[int(i) - 1].append(layer[stack_pos])

    stacks2 = deepcopy(stacks1)
    for instr in second:
        str_list = instr.split(" ")
        no = int(str_list[1])
        from_stack = stacks1[int(str_list[3]) - 1]
        to_stack = stacks1[int(str_list[5]) - 1]
        for _ in range(no):
            if from_stack:
                to_stack.append(from_stack.pop())

    for instr in second:
        str_list = instr.split(" ")
        no = int(str_list[1])
        from_stack = stacks2[int(str_list[3]) - 1]
        stacks2[int(str_list[5]) - 1] += from_stack[-no:]
        stacks2[int(str_list[3]) - 1] = from_stack[:-no]

    p1, p2 = ["".join([s[-1] for s in stack]) for stack in (stacks1, stacks2)]
    print(f"Part 1: {p1}\nPart 2: {p2}")


if __name__ == "__main__":
    solve(get_input())
