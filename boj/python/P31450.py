# https://www.acmicpc.net/problem/31450
# 2026-02-12 / 31450. Everyone is a winner / Bronze V

M, K = map(int, input().split())
print("No" if M % K else "Yes")
