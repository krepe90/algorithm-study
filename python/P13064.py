# https://www.acmicpc.net/problem/13064
# 2025-08-16 / 13064. Cameras / Bronze II

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = "123456789"

for _ in range(int(input())):
    s = input()
    if len(s) != 8:
        continue
    if s[0] != s[1]:
        continue
    for i in range(0, 8):
        if i == 4 and s[i] in c:
            continue
        elif i != 4 and s[i] in d:
            continue
        break
    else:
        print(s)
