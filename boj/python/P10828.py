# https://www.acmicpc.net/problem/10828
from sys import stdin
N = int(input())
stack = []
for _ in range(N):
    CMD = stdin.readline().split()
    if CMD[0] == "push":
        stack.append(CMD[1])
    elif CMD[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif CMD[0] == "size":
        print(len(stack))
    elif CMD[0] == "empty":
        print(0 if stack else 1)
    elif CMD[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
