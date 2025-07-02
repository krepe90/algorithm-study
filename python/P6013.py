# https://www.acmicpc.net/problem/6013
# 2025-07-02 / 6013. Lonesome Partners / Bronze II

from itertools import combinations as c


N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

d = 0
ans = (-1, -1)
for i1, i2 in c(range(N), 2):
    new_d = (P[i2][0] - P[i1][0]) ** 2 + (P[i2][1] - P[i1][1]) ** 2
    if new_d > d:
        d = new_d
        ans = (i1 + 1, i2 + 1)
print(*ans)
