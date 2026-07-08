# https://www.acmicpc.net/problem/12571
# 2025-07-09 / 12571. Rope Intranet (Small) / Bronze III

# 선이 교차하는 지점
# 모든 조합을 구한다
# 즉 (a1 - a2) * (b1 - b2) 가 음수면 겹침

from itertools import combinations as c
T = int(input())
for i in range(1, T + 1):
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    answer = 0
    for (a1, b1), (a2, b2) in c(P, 2):
        if (a1 - a2) * (b1 - b2) < 0:
            answer += 1
    print(f"Case #{i}: {answer}")
