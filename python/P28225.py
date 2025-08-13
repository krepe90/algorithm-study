# https://www.acmicpc.net/problem/28225
# 2025-08-14 / 28225. Flower Festival / Bronze III

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

# 1..n 의 차량 n대
# 가장 먼저 Rose square 에 도착하는 차량
# 교통정보 카메라, 모든 차량 위치, 속도.

t_min, i_min = 10000, 0
n, f = map(int, input().split())
for i in range(1, n + 1):
    # x: loc, v: speed
    x, v = map(int, input().split())
    t = (f - x) / v
    if t_min > t:
        t_min = t
        i_min = i
print(i_min)
