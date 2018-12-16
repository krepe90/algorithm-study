# Solved
# https://www.acmicpc.net/problem/2839


# Solution 1
n = int(input())
for i in range(int(n / 5), -1, -1):
    if (n - (i * 5)) % 3 == 0:
        print(i + int((n - (i * 5)) / 3))
        break
else:
    print(-1)
