# https://www.acmicpc.net/problem/8912
# 2026-02-16 / 8912. Sales / Bronze II

for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    B = [0] * (len(A) - 1)
    for i in range(1, len(A)):
        B[i - 1] = sum(1 for n in A[:i] if n <= A[i])
    print(sum(B))
