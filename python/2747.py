# Solved
# https://www.acmicpc.net/problem/2747


# Solution 1
val = [0, 1]
n = int(input())
if n < 2:
    print(val[n])
else:
    for i in range(2, n + 1):
        val.append(val[i - 1] + val[i - 2])
    print(val[n])
