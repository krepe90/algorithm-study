# https://www.acmicpc.net/problem/11637
# 2025-07-12 / 11637. 인기 투표 / Silver V


T = int(input())
for _ in range(T):
    n = int(input())
    r = [int(input()) for _ in range(n)]
    s = sum(r)
    mx = max(r)
    mx_i = r.index(mx) + 1
    if r.count(mx) > 1:
        print("no winner")
    elif mx > (s / 2):
        print(f"majority winner {mx_i}")
    else:
        print(f"minority winner {mx_i}")
