# https://www.acmicpc.net/problem/1018
N, M = map(int, input().split())
B = [input() for n in range(N)]
C = [[0] * M for n in range(N)]
D = [[0] * M for n in range(N)]

T = "BW"
for i in range(N):
    for j in range(M):
        if T[(i + j) % 2] != B[i][j]:
            C[i][j] = 1
T = "WB"
for i in range(N):
    for j in range(M):
        if T[(i + j) % 2] != B[i][j]:
            D[i][j] = 1

res = []
for y in range(N - 7):
    for x in range(M - 7):
        res.append(sum(sum(n[x: x + 8]) for n in C[y: y + 8]))
        res.append(sum(sum(n[x: x + 8]) for n in D[y: y + 8]))
print(min(res))
