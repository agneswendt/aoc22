from math import dist


def get_input():
    with open("input/9.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1].split(" ") for c in lines]


def solve(data):
    for p, tail in enumerate((2, 10)):
        pos = [(0, 0) for _ in range(tail)]
        visited = set()
        for instr in data:
            dir, num = instr[0], int(instr[1])
            match dir:
                case "U":
                    pull = (0, 1)
                case "D":
                    pull = (0, -1)
                case "R":
                    pull = (1, 0)
                case "L":
                    pull = (-1, 0)
            for _ in range(num):
                pos[0] = (pos[0][0] + pull[0], pos[0][1] + pull[1])
                for i in range(1, len(pos)):
                    if (
                        -1 <= pos[i][0] - pos[i - 1][0] <= 1
                        and -1 <= pos[i][1] - pos[i - 1][1] <= 1
                    ):
                        continue
                    min_dist = float("inf")
                    min_step = (0, 0)
                    for step in (
                        (0, 1),
                        (0, -1),
                        (1, 0),
                        (-1, 0),
                        (1, 1),
                        (-1, 1),
                        (1, -1),
                        (-1, -1),
                    ):
                        step_dist = dist(
                            (pos[i][0] + step[0], pos[i][1] + step[1]),
                            pos[i - 1],
                        )
                        if step_dist < min_dist:
                            min_dist = step_dist
                            min_step = step
                    pos[i] = (pos[i][0] + min_step[0], pos[i][1] + min_step[1])
                visited.add(pos[-1])
        print(f"Part {p+1}: {len(visited)}")


if __name__ == "__main__":
    solve(get_input())
