# https://www.acmicpc.net/problem/4573
# 2025-08-23 / 4573. Pizza Pricing / Bronze I

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())
i = 0
while True:
    n = int(input())
    if not n:
        break
    i += 1

    min_d, max_v = 0, 0
    for _ in range(n):
        d, p = map(int, input().split())
        v = d**2 / p
        if v > max_v:
            min_d = d
            max_v = v
    print(f"Menu {i}: {min_d}")
