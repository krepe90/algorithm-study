# https://www.acmicpc.net/problem/12537
# 2025-08-31 / 12537. Closing the Loop (Small) / Silver V

# B와 R 끈을 번갈아가며 매듭을 묶어 최대한 길게(?) 늘이기
# 매듭을 묶을 때는 각 끈에서 0.5cm씩 소모

# B, R 중 하나의 합이 0인 경우: 0
# B == R -> L - (B+R)


N = int(input())
for n in range(N):
    _ = input()
    _ropes = input().split()
    ropes_r = []
    ropes_b = []
    for r in _ropes:
        if r[-1] == "R":
            ropes_r.append(int(r[:-1]))
        else:
            ropes_b.append(int(r[:-1]))
    ropes_r.sort(reverse=True)
    ropes_b.sort(reverse=True)
    pair = min(len(ropes_b), len(ropes_r))
    ans = sum(ropes_b[:pair] + ropes_r[:pair]) - pair * 2
    print(f"Case #{n + 1}: {ans}")
