from string import ascii_lowercase


def get_input():
    with open("input/12.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


def solve(data):
    S, E = None, None
    a_list = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "S":
                S = (x, y)
                data[y] = data[y].replace("S", "a")
            elif data[y][x] == "E":
                E = (x, y)
                data[y] = data[y].replace("E", "z")
            elif data[y][x] == "a":
                a_list.append((x, y))
    print(f"Part 1: {findpath(S, E, data)}")
    print(f"Part 2: {min(map(lambda x: findpath(x, E, data), a_list))}")


def findpath(start, end, data):
    visited = {start}
    queue = [start]
    distances = {start: 0}
    while queue:
        v = queue.pop(0)
        if v == end:
            return distances[end]
        x, y = v
        current_index = ascii_lowercase.find(data[y][x])
        for curr_x, curr_y in (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ):
            if (
                0 <= curr_x < len(data[0])
                and 0 <= curr_y < len(data)
                and (curr_x, curr_y) not in visited
            ):
                if (
                    ascii_lowercase.find(data[curr_y][curr_x]) - current_index
                    <= 1
                ):
                    visited.add((curr_x, curr_y))
                    queue.append((curr_x, curr_y))
                    distances[(curr_x, curr_y)] = distances[v] + 1
    return float("inf")


if __name__ == "__main__":
    solve(get_input())
