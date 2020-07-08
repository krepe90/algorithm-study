# https://www.acmicpc.net/problem/1978
N = int(input())
NUM = map(int, input().split())

Eratos = [False, False] + [True] * 999
for i in range(2, 1001):
    if Eratos[i]:
        for j in range(i * 2, 1001, i):
            Eratos[j] = False
P = set(i for i, b in enumerate(Eratos) if b)

print(sum(1 for n in NUM if n in P))
