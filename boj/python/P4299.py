# https://www.acmicpc.net/problem/4299
# 2026-02-19 / 4299. AFC 윔블던 / Bronze IV

# a + b = s
# a - b = d

# a + b = 3
# a - b = 2
# 2b = 1

s, d = map(int, input().split())
if s + d < 0 or s - d < 0 or (s + d) & 0x01:
    print(-1)
else:
    print((s + d) // 2, (s - d) // 2)
