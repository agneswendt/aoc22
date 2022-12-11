from itertools import groupby


def get_input():
    with open("input/11.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


class monkey:
    def __init__(
        self, items: list, op: str, test: str, m1: int, m2: int
    ) -> None:
        self.items = items
        self.op = op
        self.test = test
        self.m1 = m1
        self.m2 = m2
        self.score = 0


def solve(data):
    monkeys_raw = [
        list(g) for k, g in groupby(data, lambda x: x == "") if not k
    ]
    score = [0 for _ in range(len(monkeys_raw))]

    monkeys = []
    for m in monkeys_raw:
        monkeys.append(
            monkey(
                items=list(map(int, m[1].split(": ")[-1].split(", "))),
                op=m[2].split(": ")[-1].split("=")[-1],
                test=int(m[3].split(" ")[-1]),
                m1=int(m[4].split(" ")[-1]),
                m2=int(m[5].split(" ")[-1]),
            )
        )

    for _ in range(10000):
        for m in monkeys:
            for item in m.items:
                m.score += 1
                old = item
                new = eval(m.op) % 9699690  # 🤡
                if new % m.test:
                    monkeys[m.m2].items.append(new)
                else:
                    monkeys[m.m1].items.append(new)
            m.items = []
    score = list(reversed(sorted(m.score for m in monkeys)))
    print(f"Part 2: {score[0] * score[1]}")


if __name__ == "__main__":
    solve(get_input())
