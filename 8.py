def get_input():
    with open("input/8.txt", "r") as f:
        lines = f.readlines()
    return [list(map(int, c[:-1])) for c in lines]


def sight(trees, x, y):
    tree = trees[y][x]
    a, b, c, d = [0] * 4
    visible = False
    for i in range(x-1, -1, -1):
        a += 1
        if trees[y][i] >= tree:
            break
    else: visible = True
    for i in range(x + 1, len(trees[0])):
        b += 1
        if trees[y][i] >= tree:
            break
    else: visible = True
    for i in range(y-1, -1, -1):
        c += 1
        if trees[i][x] >= tree:
            break
    else: visible = True
    for i in range(y + 1, len(trees)):
        d += 1
        if trees[i][x] >= tree:
            break
    else: visible = True
    return visible, a * b * c * d


def solve(data):
    p1 = 0
    p2 = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            visible, tree_sight = sight(data, x, y)
            p1 += visible
            if tree_sight > p2:
                p2 = tree_sight
    print(f"Part 1: {p1}\nPart 2: {p2}")


if __name__ == "__main__":
    solve(get_input())
