# https://www.acmicpc.net/problem/2164
N = int(input())
A = list(range(1, N + 1))
x = 0
while len(A) > 1:
    last = A[-1]
    A = [n for i, n in enumerate(A) if (i + x) % 2]
    if last != A[-1]:
        x = 1
    else:
        x = 0
print(A[0])
