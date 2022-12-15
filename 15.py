def get_input():
    with open("input/15.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


def solve(data):
    sensors = []
    beacons = []
    for line in data:
        _, s, b = line.split("at ")
        s_x, s_y = s.split(": ")[0].split(", ")
        sensor = int(s_x.split("=")[-1]), int(int(s_y.split("=")[-1]))
        sensors.append(sensor)
        b_x, b_y = b.split(", ")
        beacon = int(b_x.split("=")[-1]), int(int(b_y.split("=")[-1]))
        beacons.append(beacon)

    upper = 4000000
    for y in range(upper):
        x = 0
        while x < (upper):
            changed = False
            for s, b in zip(sensors, beacons):
                dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
                if abs(s[0]-x) + abs(s[1]-y) < dist:
                    x += (dist - abs(s[1]-y) - abs(s[0]-x))
                    changed = True
                elif abs(s[0]-x) + abs(s[1]-y) == dist:
                    x += 1
                    changed = True
            if not changed:
                print("Part 2:", x * 4000000 + y)
                return


if __name__ == "__main__":
    import time

    start = time.time()
    solve(get_input())
    print("Time:", time.time() - start)
