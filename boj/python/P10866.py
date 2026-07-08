# https://www.acmicpc.net/problem/10866
from sys import stdin
from collections import deque
N = int(input())
dq = deque()
for _ in range(N):
    CMD = stdin.readline().split()
    if CMD[0] == "push_front":
        dq.appendleft(CMD[1])
    if CMD[0] == "push_back":
        dq.append(CMD[1])
    elif CMD[0] == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif CMD[0] == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif CMD[0] == "size":
        print(len(dq))
    elif CMD[0] == "empty":
        print(0 if dq else 1)
    elif CMD[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif CMD[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
