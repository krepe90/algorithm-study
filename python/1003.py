# Solved
# https://www.acmicpc.net/problem/1003


# Solution 1
val = []
for cnt in range(int(input())):
    val += [int(input())]
for n in val:
    if n == 0:
        print(1, 0)
        continue
    elif n == 1:
        print(0, 1)
        continue
    ret = {0: 0, 1: 1}
    for i in range(2, n + 1):
        ret[i] = ret[i - 1] + ret[i - 2]
    print(ret[n - 1], ret[n])
