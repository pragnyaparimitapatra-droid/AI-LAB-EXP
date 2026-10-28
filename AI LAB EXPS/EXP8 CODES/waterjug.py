from collections import deque

def water_jug(a, b, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == target or y == target:
            print("Target achieved!")
            return

        queue.append((a, y))
        queue.append((x, b))
        queue.append((0, y))
        queue.append((x, 0))

        pour = min(x, b - y)
        queue.append((x - pour, y + pour))

        pour = min(y, a - x)
        queue.append((x + pour, y - pour))

    print("No solution exists")


a = int(input("Enter capacity of jug A: "))
b = int(input("Enter capacity of jug B: "))
target = int(input("Enter target amount: "))

water_jug(a, b, target)