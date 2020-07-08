# https://www.acmicpc.net/problem/1654
N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

length = 2 ** 30 - 1
s = 0
while s < 28:
    cnt = sum(i // length for i in A)

    if cnt < K:
        # print(f"- {length} / {cnt}")
        length -= round(pow(2, 29 - s))
    else:
        # print(f"+ {length} / {cnt}")
        length += round(pow(2, 29 - s))
    s += 1

print(max(n for n in range(length - 8, length + 8) if n > 0 and sum(i // n for i in A) >= K))
