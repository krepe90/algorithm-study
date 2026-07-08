# https://www.acmicpc.net/problem/27969
# 2025-07-01 / 27969. I LOVE JavaScript / Silver III

ans = 0
for w in input().split():
    if w == "[" or w.isdigit():
        ans += 8
    elif w != "]":
        ans += len(w) + 12
print(ans)
