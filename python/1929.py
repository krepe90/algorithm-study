# https://www.acmicpc.net/problem/1929
M, N = map(int, input().split())

Eratos = [False, False] + [True] * (N - 1)
for i in range(2, N + 1):
    if Eratos[i]:
        for j in range(i * 2, N + 1, i):
            Eratos[j] = False
P = (str(i) for i, b in enumerate(Eratos) if b and i >= M)
print("\n".join(P))
