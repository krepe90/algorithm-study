# https://www.acmicpc.net/problem/24246
# 2025-08-12 / 24246. Junior price robot / Bronze II

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

N = int(input())
arr = map(int, input().split())
today = next(arr)
for i, p in enumerate(arr, 1):
    if p <= today:
        print(i)
        break
else:
    print("infinity")
