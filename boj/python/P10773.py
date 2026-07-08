import sys

K = int(sys.stdin.readline())
L = []
for _ in range(K):
    i = int(sys.stdin.readline())
    if i:
        L.append(i)
    else:
        L.pop()
print(sum(L))
