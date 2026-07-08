# https://www.acmicpc.net/problem/14038
# 2026-02-22 / 14038. Tournament Selection / Bronze IV

results = [input() for _ in range(6)]
wins = results.count("W")
if wins >= 5:
    print(1)
elif wins >= 3:
    print(2)
elif wins >= 1:
    print(3)
else:
    print(-1)
