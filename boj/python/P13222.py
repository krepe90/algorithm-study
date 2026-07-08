# https://www.acmicpc.net/problem/13222
# 2025-08-08 / 13222. Matches / Bronze III

N, W, H = map(int, input().split())
L = (W * W + H * H) ** 0.5
for _ in range(N):
    print("YES" if int(input()) <= L else "NO")
