# https://www.acmicpc.net/problem/27370
# 2025-07-29 / 27370. 친구와 배달하기 / Silver III

# 가까운 쪽으로 할당시켜주면 된다.
# 단, 정중앙이면 일 덜한 쪽으로

T = int(input())
for _ in range(T):
    N, P_A, P_B = map(int, input().split())
    dst_list = list(map(int, input().split()))

    P_A, P_B = (P_A, P_B) if P_A < P_B else (P_B, P_A)

    middle = (P_A + P_B) / 2
    middle_count = 0
    dist_l = dist_r = 0
    for p in dst_list:
        if p < middle:
            dist_l += (p - P_A) * 2
        elif middle < p:
            dist_r += (P_B - p) * 2
        else:
            middle_count += 1
    for _ in range(middle_count):
        if dist_l < dist_r:
            dist_l += (P_B - middle) * 2
        else:
            dist_r += (P_B - middle) * 2
    print(int(dist_l + dist_r), int(abs(dist_l - dist_r)))
