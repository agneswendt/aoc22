from string import ascii_lowercase, ascii_uppercase


def get_input():
    with open("input/3.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


def solve(data):
    p1 = 0
    char_str = ascii_lowercase + ascii_uppercase
    for item in data:
        first, second = set(item[:len(item) // 2]), set(
            item[len(item) // 2:]
        )
        for c in first.intersection(second):
            p1 += char_str.index(c) + 1
            break

    p2 = 0
    for elems in zip(*[iter(data)] * 3):
        x, y, z = map(set, elems)
        common = x.intersection(y.intersection(z))
        for c in common:
            p2 += char_str.index(c) + 1
            break

    print(f"Part 1: {p1}\nPart 2: {p2}")


if __name__ == "__main__":
    solve(get_input())
