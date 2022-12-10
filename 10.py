def get_input():
    with open("input/10.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


def solve(data):
    i = 0
    addx = False
    x = 1
    p1 = 0
    cycles = 0
    while i < len(data):
        instr, *val = data[i].split(" ")
        cycles += 1
        if cycles in range(20, 221, 40):
            p1 += cycles * x
        if val:
            assert instr == "addx"
            if addx:
                x += int(val[0])
                addx = False
                i += 1
            else:
                addx = True
        else:
            assert instr == "noop"
            i += 1
        if cycles in range(40, 241, 40):
            print()
        if cycles % 40 - 1 <= x <= cycles % 40 + 1:
            print("#", end="")
        else:
            print(".", end="")
    print(f"\nPart 1: {p1}")


if __name__ == "__main__":
    solve(get_input())
