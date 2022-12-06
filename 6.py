def get_input():
    with open("input/6.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines][0]


def solve(data):
    p1, p2 = [
        [
            i + msg_len
            for i in range(len(data))
            if len(set(data[i: i + msg_len])) == msg_len
        ][0]
        for msg_len in (4, 14)
    ]
    print(f"Part 1: {p1}\nPart 2: {p2}")


if __name__ == "__main__":
    solve(get_input())
