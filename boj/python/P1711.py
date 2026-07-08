# a**2 + b**2 = c**2
import typing
P: typing.TypeAlias = tuple[int, int]

import sys

input = lambda: sys.stdin.readline().rstrip()
def dist(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(len(p) - 2):
    for j in range(i + 1, len(p) - 1):
        for k in range(j + 1, len(p)):
            d1, d2, d3 = dist(p[i], p[j]), dist(p[j], p[k]), dist(p[i], p[k])
            if max(d1, d2, d3) * 2 == (d1 + d2 + d3):
                result += 1
print(result)
