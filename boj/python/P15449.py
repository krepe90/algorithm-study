# https://www.acmicpc.net/problem/15449
# 2025-07-31 / 15449. Art / Bronze II

from itertools import combinations as c


answer = 0
for lengths in c(map(int, input().split()), 3):
    x, y, z = sorted(lengths)
    if x + y > z:
        answer += 1
print(answer)
