# https://www.acmicpc.net/problem/2669
# 2025-07-19 / 2669. 직사각형 네개의 합집합의 면적 구하기 / Silver V

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

plane = [0] * 101 * 101
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            plane[y * 101 + x] = 1
print(sum(plane))
