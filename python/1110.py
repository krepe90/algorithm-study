# https://www.acmicpc.net/problem/1110
N = int(input())
cnt = 0
a, b = N // 10, N % 10
while True:
    a, b = b, (a + b) % 10
    cnt += 1
    if (a * 10 + b) == N:
        break
print(cnt)
