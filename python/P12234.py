# https://www.acmicpc.net/problem/12234
# 2025-07-07 / 12234. Data Packing (Small) / Silver IV

# X가 CD 용량, S_i 가 파일 크기

T = int(input())
for i in range(1, T + 1):
    N, X = map(int, input().split())
    S = list(map(int, input().split()))
    S.sort()

    count = 0
    while S:
        last = S.pop()
        count += 1
        if S and S[0] + last <= X:
            S.pop(0)

    print(f"Case #{i}: {count}")
