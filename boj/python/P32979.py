# https://www.acmicpc.net/problem/32979
# 2025-08-04 / 32979. 아파트 / Silver V

N = int(input())
T = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0
results = []
for j in range(T):
    i = (i + B[j] - 1) % (2 * N)
    results.append(A[i])
print(*results)
