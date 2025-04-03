N = int(input())
a = [
    list(map(int, input().split()))
    for _ in range(N)
]
r = [0] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        r[i] = r[i] | a[i][j]
print(*r)
