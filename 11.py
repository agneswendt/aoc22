from itertools import groupby


def get_input():
    with open("input/11.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


def solve(data):
    monkeys_raw = [
        list(g) for k, g in groupby(data, lambda x: x == "") if not k
    ]
    score = [0 for _ in range(len(monkeys_raw))]
    monkeys = {}
    for i, m in enumerate(monkeys_raw):
        monkeys[i] = {
            "items": list(map(int, m[1].split(": ")[-1].split(", "))),
            "operation": m[2].split(": ")[-1].split("=")[-1],
            "test": int(m[3].split(" ")[-1]),
            "m1": int(m[4].split(" ")[-1]),
            "m2": int(m[5].split(" ")[-1]),
        }

    for _ in range(10000):
        for m in monkeys:
            for i, item in enumerate(monkeys[m]["items"]):
                score[m] += 1
                old = item
                # new = eval(monkeys[m]["operation"]) // 3
                new = eval(monkeys[m]["operation"]) % 9699690  # 🤡
                if new % monkeys[m]["test"]:
                    monkeys[monkeys[m]["m2"]]["items"].append(new)
                else:
                    monkeys[monkeys[m]["m1"]]["items"].append(new)
            monkeys[m]["items"] = []
    score = list(reversed(sorted(score)))
    print(f"Part 2: {score[0] * score[1]}")


if __name__ == "__main__":
    solve(get_input())
