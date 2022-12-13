from itertools import groupby
from functools import cmp_to_key


def get_input():
    with open("input/13.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


def solve(data):
    packets = [list(g) for k, g in groupby(data, lambda x: x == "") if not k]
    res = 0
    packet_list = []
    for i, (p1, p2) in enumerate(packets):
        if traverse(eval(p1), eval(p2)):
            res += i + 1
        packet_list += [eval(p1), eval(p2)]
    packet_list += [[[2]], [[6]]]

    packet_list.sort(
        key=cmp_to_key(lambda p1, p2: 1 if traverse(p1, p2) else -1),
        reverse=True,
    )
    print(f"Part 1: {res}")
    print(
        f"Part 2: {((packet_list.index([[2]])+1) * (packet_list.index([[6]])+1))}"
    )


def traverse(p1, p2):
    if not p1 and p2:
        return True
    elif p1 and not p2:
        return False
    if not p1 and not p2:
        return None
    left, *p1 = p1
    right, *p2 = p2
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
        elif left == right:
            return traverse(p1, p2)
    elif isinstance(left, list) and isinstance(right, list):
        list_res = traverse(left, right)
        if list_res is None:
            return traverse(p1, p2)
        else:
            return list_res
    else:
        if isinstance(left, int):
            return traverse([left], right)
        else:
            return traverse(left, [right])


if __name__ == "__main__":
    solve(get_input())
