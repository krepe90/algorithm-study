# https://www.acmicpc.net/problem/1966
from sys import stdin
for _ in range(int(input())):
    N, M = map(int, stdin.readline().split())
    q = list(map(int, stdin.readline().split()))
    cnt = 0
    while True:
        if q[0] >= max(q):
            q.pop(0)
            cnt += 1
            if M == 0:
                break
            else:
                M -= 1
        else:
            q.append(q.pop(0))
            if M == 0:
                M = len(q) - 1
            else:
                M -= 1
    print(cnt)
