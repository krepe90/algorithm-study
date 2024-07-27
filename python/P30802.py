# https://www.acmicpc.net/problem/30802
# 웰컴 키트
# Solved.ac CLASS 2*

import math


N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum(math.ceil(n / T) for n in sizes))
print(f"{N // P} {N % P}")
