# https://www.acmicpc.net/problem/10845
from sys import stdin
N = int(input())
queue = []
for _ in range(N):
    CMD = stdin.readline().split()
    if CMD[0] == "push":
        queue.append(CMD[1])
    elif CMD[0] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif CMD[0] == "size":
        print(len(queue))
    elif CMD[0] == "empty":
        print(0 if queue else 1)
    elif CMD[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif CMD[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
