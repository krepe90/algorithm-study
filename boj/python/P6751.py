# https://www.acmicpc.net/problem/6751
# 2025-08-21 / 6751. From 1987 to 2013 / Bronze II

for y in range(int(input()) + 1, 10235):
    s = str(y)
    if len(set(s)) == len(s):
        print(y)
        break
