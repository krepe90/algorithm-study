# https://www.acmicpc.net/problem/10250
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    print(f"{(N - 1) % H + 1}{(N - 1) // H + 1:02}")
