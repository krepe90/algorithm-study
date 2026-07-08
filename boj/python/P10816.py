# https://www.acmicpc.net/problem/10816
D = dict()
N = int(input())
for n in map(int, input().split()):
    D[n] = D.get(n, 0) + 1
M = int(input())
A = map(int, input().split())
print(" ".join(str(D.get(n, 0)) for n in A))
