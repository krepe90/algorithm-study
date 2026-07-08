# https://www.acmicpc.net/problem/10656
# 2025-09-17 / 10656. 십자말풀이 / Silver IV

# 방문지점은 시작지점이 될 수 없어

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

visited_v = [[False] * M for _ in range(N)]
visited_h = [[False] * M for _ in range(N)]
start_points = []
for j in range(N):
    for i in range(M):
        x, y = i, j
        if not visited_h[j][i]:
            while x < M and arr[j][x] == ".":
                visited_h[j][x] = True
                x += 1
        if not visited_v[j][i]:
            while y < N and arr[y][i] == ".":
                visited_v[y][i] = True
                y += 1
        if x - i >= 3 or y - j >= 3:
            start_points.append(f"{j + 1} {i + 1}")
print(len(start_points))
print(*start_points, sep="\n")
