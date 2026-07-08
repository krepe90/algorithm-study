# https://www.acmicpc.net/problem/1358
# 2025-07-20 / 1358. 하키 / Silver IV

import math

W, H, X, Y, P = map(int, input().split())
x1, x2 = X, X + W
y1, y2 = Y, Y + H
r = H // 2

answer = 0
for _ in range(P):
    x, y = map(int, input().split())
    if x1 <= x <= x2 and y1 <= y <= y2:
        answer += 1
    elif math.dist((x, y), (x1, y1 + r)) <= r or math.dist((x, y), (x2, y1 + r)) <= r:
        answer += 1
print(answer)
