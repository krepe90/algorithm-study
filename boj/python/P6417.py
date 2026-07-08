# https://www.acmicpc.net/problem/6417
# 2025-06-23 / 6417. 코코넛 그 두 번째 이야기 / Silver IV

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

def check(n: int, k: int):
    for _ in range(k):
        if n % k != 1:
            return False
        n = n // k * (k - 1)
    else:
        return True


while (n := int(input())) != -1:
    ans = 0
    for k in range(2, n):
        if check(n, k):
            ans = k
    print(f"{n} coconuts, {ans} people and 1 monkey" if ans else f"{n} coconuts, no solution")

