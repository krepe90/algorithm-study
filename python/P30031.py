# https://www.acmicpc.net/problem/30031
# 2025-08-27 / 30031. 지폐 세기 / Bronze IV

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

d = {"136": 1, "142": 5, "148": 10, "154": 50}
print(sum(d[input().split()[0]] for _ in range(int(input()))) * 1000)
