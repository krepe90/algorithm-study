#  첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)
# 둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

# 최소 시간과 높이 출력
# 블럭 제거 2초, 블럭 배치 1초
N, M, B = map(int, input().split())
a: list[int] = []
for _ in range(N):
    a.extend(map(int, input().split()))

mn, mx = min(a), max(a)
result = []
for h in range(mn, mx+1):
    # 양수면 블럭 배치 필요, 음수면 블럭 제거 필요
    p, r = 0, 0
    for n in a:
        v = h - n
        if v > 0:
            p += v
        else:
            r -= v
    # 가진 블럭이 부족하면 스킵
    if (p - r) > B:
        continue
    result.append((p+r*2, h))
result.sort(key=lambda x: (-x[0], x[1]))
print(*result[-1])
