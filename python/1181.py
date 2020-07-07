# https://www.acmicpc.net/problem/
N = int(input())
A = set()
for i in range(N):
    A.add(input())
print("\n".join(sorted(A, key=lambda x: (len(x), x))))
