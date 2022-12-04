def get_input():
    with open("input/4.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1].split(",") for c in lines]


def solve(data):
    p1 = 0
    p2 = 0
    for a, b in data:
        l1, u1 = map(int, a.split("-"))
        l2, u2 = map(int, b.split("-"))
        r1 = set(range(l1, u1 + 1))
        r2 = set(range(l2, u2 + 1))

        if r1 <= r2 or r2 <= r1:
            p1 += 1
        if r1 & r2 or r2 & r1:
            p2 += 1

    print(f"Part 1: {p1}\nPart 2: {p2}")


if __name__ == "__main__":
    solve(get_input())
