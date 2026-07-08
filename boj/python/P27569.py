# https://www.acmicpc.net/problem/27569
# 2025-09-02 / 27569. Champernowne Count / Silver III

x = 0
ans = 0
n, k = map(int, input().split())
for i in range(1, n + 1):
    d = len(str(i))
    x = (x * 10**d + i) % k
    if x == 0:
        ans += 1
print(ans)
