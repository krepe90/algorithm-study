# https://www.acmicpc.net/problem/8911
# 2025-07-28 / 8911. 거북이 / Silver III

T = int(input())
for _ in range(T):
    d_list = [
        (0, 1),  # 북
        (1, 0),  # 동
        (0, -1),  # 남
        (-1, 0),  # 서
    ]

    d = 0
    x = y = 0
    max_x = max_y = min_x = min_y = 0
    for c in input():
        match c:
            case "F":
                dx, dy = d_list[d]
                x += dx
                y += dy
            case "B":
                dx, dy = d_list[d]
                x -= dx
                y -= dy
            case "L":
                d = (d - 1) % 4
            case "R":
                d = (d + 1) % 4
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    print((max_x - min_x) * (max_y - min_y))
