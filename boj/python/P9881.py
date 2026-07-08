# https://www.acmicpc.net/problem/9881
# 2026-02-18 / 9881. Ski Course Design / Silver V

# 고저차가 17 이하가 되는 최소치
# 1. 정렬
# 2. 연산
# 조금 더 최적화 하면 0~100 배열을 만들어서 갯수를 기록하고 그 갯수로 범위를 재면 되긴 하는데 귀찮다


def calc(arr: list[int], h: int):
    left = sum(((h - n) ** 2 for n in arr if n < h))
    right = sum(((n - h - 17) ** 2 for n in arr if n > h + 17))
    return left + right


N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
mn = A[0]
mx = A[-1]

results = [calc(A, i) for i in range(mn, mx - 17)]
print(min(results) if results else 0)
