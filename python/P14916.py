# https://www.acmicpc.net/problem/14916
# 2025-08-26 / 14916. 거스름돈 / Silver V

n = int(input())

c2 = 0
c5 = 0
while n >= c2 * 2:
    if (n - c2 * 2) % 5 == 0:
        c5 = (n - c2 * 2) // 5
        break
    c2 += 1
print(c2 + c5 if n >= c2 * 2 else -1)
