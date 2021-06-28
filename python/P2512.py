import math


def cut(arr, cutline):
    return sum(n if n < cutline else cutline for n in arr)


N = int(input())
L = n = [int(n) for n in input().split()]
M = int(input())

# 1. 모든 예산의 합이 M보다 작은 경우 프로그램 끝
s = sum(L)
if s <= M:
    print(max(L))
else:
    # 이분 탐색 코드
    pass
