# https://www.acmicpc.net/problem/27512
# 2025-07-30 / 27512. 스네이크 / Bronze II

W, H = map(int, input().split())
print(W * H & 0xFFFE)
