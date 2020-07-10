# https://www.acmicpc.net/problem/11050
from functools import reduce
N, K = map(int, input().split())
a = reduce(lambda x, y: x * y, range(N - K + 1, N + 1)) if N and K else 1
b = reduce(lambda x, y: x * y, range(1, K + 1)) if K else 1
print(a // b)
