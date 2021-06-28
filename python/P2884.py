# https://www.acmicpc.net/problem/2884
H, M = map(int, input().split())
M -= 45
if M < 0:
    H -= 1
print(f"{H % 24} {M % 60}")
