# https://www.acmicpc.net/problem/9012
from sys import stdin
T = int(input())
for _ in range(T):
    stack = 0
    S = stdin.readline().rstrip()
    for c in S:
        if c == "(":
            stack += 1
        elif stack > 0:
            stack -= 1
        else:
            print("NO")
            break
    else:
        print("NO" if stack else "YES")
