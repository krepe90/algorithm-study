# https://www.acmicpc.net/problem/2869
# 달팽이는 올라가고 싶다

# 2026-02-19 스트릭 유지 용도로 사용

import math

A, B, V = map(int, input().split())

print(math.ceil((V - A) / (A - B)) + 1)
