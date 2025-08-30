# https://www.acmicpc.net/problem/8016
# 2025-08-30 / 8016. Insulator / Silver V

arr = [int(input()) for _ in range(int(input()))]
arr.sort()

ans = sum(arr)
while len(arr) > 1:
    left = arr.pop(0)
    right = arr.pop(-1)
    ans += right - left
print(ans)
