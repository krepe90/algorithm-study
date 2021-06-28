# https://www.acmicpc.net/problem/2292
n = int(input()) - 1
if n == 0:
    print(1)
else:
    step = 1
    while n > step * 6:
        n -= step * 6
        step += 1
    print(step + 1)
