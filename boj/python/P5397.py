# https://www.acmicpc.net/problem/5397

import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    L = input()
    left_stack, right_stack = list(), list()
    for c in L:
        match c:
            case "-":
                if left_stack:
                    left_stack.pop()
            case "<":
                if left_stack:
                    right_stack.append(left_stack.pop())
            case ">":
                if right_stack:
                    left_stack.append(right_stack.pop())
            case _:
                left_stack.append(c)
    print(*left_stack, *right_stack[::-1], sep="")
