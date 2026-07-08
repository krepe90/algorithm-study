# https://www.acmicpc.net/problem/31216
# 2025-08-18 / 31216. 슈퍼 소수 / Silver V

import sys

input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# N, M = map(int, input().split())

arr = [1] * 318138
prime_set = set()
for i in range(2, 318138):
    if arr[i]:
        prime_set.add(i)
        for j in range(i + i, 318138, i):
            arr[j] = 0
super_prime_list = [v for i, v in enumerate(sorted(prime_set), 1) if i in prime_set]

T = int(input())
for _ in range(T):
    print(super_prime_list[int(input()) - 1])
