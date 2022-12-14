from itertools import product


def get_input():
    with open("input/14.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1].split(" -> ") for c in lines]


def solve(data):
    rocks = set()
    for line in data:
        for i in range(len(line) - 1):
            (x1, y1), (x2, y2) = map(int, line[i].split(",")), map(int, line[i + 1].split(","))
            (min_x, max_x), (min_y, max_y) = sorted((x1, x2)), sorted((y1, y2))
            rocks |= set(
                product(range(min_x, max_x + 1), range(min_y, max_y + 1))
            )
    # brute force, tar ca en halvtimme
    # kör koden om det är kallt hemma :)
    max_y = max(rocks, key=(lambda x: x[1]))[1]
    rocks |= set((x, max_y + 2) for x in range(0, 1000))
    sand = set()
    current_sand = (500, 0)
    while (500, 0) not in sand:
        x, y = current_sand
        if (x, y + 1) in (rocks | sand):
            if (x - 1, y + 1) in (rocks | sand):
                if (x + 1, y + 1) in (rocks | sand):
                    sand.add((x, y))
                    min_sand = min(sand, key=(lambda x: x[1]))[1]
                    current_sand = (500, min_sand - 1)
                else:
                    current_sand = (x + 1, y + 1)
            else:
                current_sand = (x - 1, y + 1)
        else:
            current_sand = (x, y + 1)
    print(f"Part 2: {len(sand)}")


if __name__ == "__main__":
    solve(get_input())
