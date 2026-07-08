# https://www.acmicpc.net/problem/1996
# 2025-08-13 / 1996. 지뢰 찾기 / Silver V

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
mine = [[int(c) if c.isdigit() else 0 for c in input()] for _ in range(N)]

for y in range(N):
    line = []
    arr = list(map(sum, zip(*mine[max(0, y - 1) : y + 2])))
    for x in range(N):
        if mine[y][x]:
            line.append("*")
        else:
            count = sum(arr[max(0, x - 1) : x + 2])
            count_str = str(count) if count < 10 else "M"
            line.append(count_str)
    print("".join(line))
