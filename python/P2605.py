# https://www.acmicpc.net/problem/2605
# 2025-07-16 / 2605. 줄 세우기 / Bronze II

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
arr = map(int, input().split())
result = []
for num, cmd in enumerate(arr, 1):
    result.insert(num - 1 - cmd, num)
print(*result)
