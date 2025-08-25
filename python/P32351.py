# https://www.acmicpc.net/problem/32351
# 2025-08-25 / 32351. 리듬게임 / Bronze I

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

_n, _s_0, _k = input().split()
N = int(_n)
S_0 = float(_s_0)
K = int(_k)

_ans = 0.0
data = [
    (1, S_0),
]
for _ in range(K):
    _m, _s = input().split()
    m = int(_m)
    s = float(_s)

    _ans += (m - data[-1][0]) / data[-1][1]

    data.append((m, s))
_ans += (N + 1 - data[-1][0]) / data[-1][1]
ans = _ans * 240
print(f"{ans:.12f}")
