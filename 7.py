def get_input():
    with open("input/7.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]


class dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.files = []
        self.children = []

    def get_size(self):
        s = 0
        for f in self.files:
            s += f.size
        for c in self.children:
            s += c.get_size()
        return s


class file:
    def __init__(self, size, name):
        self.name = name
        self.size = int(size)


def solve(data):
    root = dir(None, "/")
    i = 0
    while i < len(data):
        if data[i].split(" ")[1] == "cd":
            name = data[i].split(" ")[-1]
            if name == "/":
                curr = root
            elif name == "..":
                curr = curr.parent if curr.parent else root
            else:
                for d in curr.children:
                    if d.name == name:
                        curr = d
                        break
        else:
            i += 1
            while "$" not in data[i] and i < len(data):
                if data[i].split(" ")[0] == "dir":
                    curr.children.append(dir(curr, data[i].split(" ")[-1]))
                else:
                    curr.files.append(file(*data[i].split(" ")))
                if i + 1 < len(data) and "$" not in data[i + 1]:
                    i += 1
                else:
                    break
        i += 1

    def p1(current):
        s = 0
        for d in current.children:
            d_size = d.get_size()
            if d_size <= 100000:
                s += d_size
            s += p1(d)
        return s

    def p2(size, current):
        curr_size = current.get_size()
        smallest, tot_size = (
            (curr_size - size, curr_size)
            if curr_size - size > 0
            else (float("inf"), float("inf"))
        )
        for c in current.children:
            curr_smallest, curr_tot_size = p2(size, c)
            if curr_smallest < smallest:
                smallest = curr_smallest
                tot_size = curr_tot_size
        return smallest, tot_size

    needed = 30000000 - (70000000 - root.get_size())
    print(f"Part 1: {p1(root)}\nPart 2: {p2(needed, root)[1]}")


if __name__ == "__main__":
    solve(get_input())
