# https://www.acmicpc.net/problem/16283
# 2025-07-17 / 16283. Farm / Bronze II

# a: 양 1마리당 사료 소모량
# b: 염소 1마리당 사료 소모량
# n: 양 + 염소 (단위: 마리)
# w: 전체 사료 소모량
# ax + by = w
# x + y = n -> y = n - x
# ax + b(n - x) = w
# ax + bn - bx = w
# (a-b)x = w - bn
# x = (w - bn) / (a - b)

# a = b 일 때, x + (n - x) = w
# n = w

# 귀찮다 브루트포스 할래 (O(N), N <= 1000)

a, b, n, w = map(int, input().split())

answer_list = []
for x in range(1, n):
    y = n - x
    if a * x + b * y == w:
        answer_list.append(x)
if len(answer_list) == 1:
    print(answer_list[0], n - answer_list[0])
else:
    print(-1)
