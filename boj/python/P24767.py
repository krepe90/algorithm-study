# https://www.acmicpc.net/problem/24767
# 2025-07-18 / 24767. Beehives / Bronze II

from itertools import combinations as c

while True:
    _d, _n = input().split()
    d = float(_d)
    n = int(_n)

    if d == 0 and n == 0:
        break

    pos_list = [tuple(map(float, input().split())) for _ in range(n)]
    sour_pos_set = set()
    for pos_a, pos_b in c(pos_list, 2):
        dist_sq = (pos_a[1] - pos_b[1]) ** 2 + (pos_a[0] - pos_b[0]) ** 2
        if dist_sq <= d**2:
            sour_pos_set.add(pos_a)
            sour_pos_set.add(pos_b)
    print(f"{len(sour_pos_set)} sour, {n - len(sour_pos_set)} sweet")
