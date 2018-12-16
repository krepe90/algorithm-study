# Solved
# https://www.acmicpc.net/problem/1002


# Solution 1
case = int(input())
ret = []
for i in range(case):
    val = input().split(" ")
    c1, c2 = (int(val[0]), int(val[1]), int(val[2])), (int(val[3]), int(val[4]), int(val[5]))
    if c1 == c2:
        ret += [-1]
        continue
    d = ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5
    if d > c1[2] and d > c2[2]:
        if c1[2] + c2[2] > d:
            ret += [2]
        elif c1[2] + c2[2] == d:
            ret += [1]
        else:
            ret += [0]
    else:
        if abs(c1[2] - c2[2]) < d:
            ret += [2]
        elif abs(c1[2] - c2[2]) == d:
            ret += [1]
        else:
            ret += [0]
for j in ret:
    print(j)
