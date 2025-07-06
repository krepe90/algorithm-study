# https://www.acmicpc.net/problem/14492
# 2025-07-06 / 14492. 부울행렬의 부울곱 / Silver V

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(N):
        for n in range(N):
            if A[i][n] and B[n][j]:
                answer += 1
                break
print(answer)
