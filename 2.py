def get_input():
    with open("input/2.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1].split(" ") for c in lines]


def solve(data):
    losing = {"A": "Z", "B": "X", "C": "Y"}
    tie = {"A": "X", "B": "Y", "C": "Z"}
    winning = {"A": "Y", "B": "Z", "C": "X"}

    sign_points = {"X": 1, "Y": 2, "Z": 3}

    p1 = 0
    for a, b in data:
        p1 += sign_points[b]
        if tie[a] == b:
            p1 += 3
        elif winning[a] == b:
            p1 += 6

    points = {"X": 0, "Y": 3, "Z": 6}
    outcome = {"X": losing, "Y": tie, "Z": winning}
    p2 = sum(points[b] + sign_points[outcome[b][a]] for a, b in data)
    print(f"Part 1: {p1}\nPart 2: {p2}")


if __name__ == "__main__":
    solve(get_input())
