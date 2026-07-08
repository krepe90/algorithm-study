# https://www.acmicpc.net/problem/25595
# 2025-08-01 / 25595. 86 ─에이티식스─ 2 / Bronze I

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

even, odd = 0, 0
is_odd = -1
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            if (r + c) & 0x01:
                odd += 1
            else:
                even += 1
        elif arr[r][c] == 2:
            is_odd = (r + c) & 0x01

if (is_odd and odd) or (not is_odd and even):
    print("Kiriya")
else:
    print("Lena")
