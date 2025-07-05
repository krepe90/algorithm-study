# https://www.acmicpc.net/problem/3566
# 2025-07-05 / 3566. 대형 스크린 / Bronze I

# (resolution|size)_(horizontal|vertical)
from math import ceil


rh, rv, sh, sv = map(int, input().split())
n = int(input())
answer = 2 ** 31 - 1
for _ in range(n):
    rh_i, rv_i, sh_i, sv_i, p = map(int, input().split())
    total_h = max(ceil(rh / rh_i), ceil(sh / sh_i)) * max(ceil(rv / rv_i), ceil(sv / sv_i)) * p
    total_v = max(ceil(rh / rv_i), ceil(sh / sv_i)) * max(ceil(rv / rh_i), ceil(sv / sh_i)) * p
    total = min(total_h, total_v)
    if total < answer:
        answer = total
print(answer)
