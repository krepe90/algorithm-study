# https://www.acmicpc.net/problem/16967
# 2025-07-21 / 16967. 배열 복원하기 / Silver III

# A : [0..H, 0..W]
# A': [X..X+H, Y..Y+W]

H, W, X, Y = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H + X)]
A = []
for i in range(H):
    arr = [B[i][j] if i < X or j < Y else B[i][j] - A[i - X][j - Y] for j in range(W)]
    A.append(arr)
    print(*arr)
