# https://www.acmicpc.net/problem/2798
# 전체적으로 비효율적인 풀이. 3중 반복문이라니;;
from array import array
N, M = map(int, input().split())
A = array("i", map(int, input().split()))
V = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            s = A[i] + A[j] + A[k]
            if V < s and s <= M:
                V = s
    if V == M:
        break
print(V)
