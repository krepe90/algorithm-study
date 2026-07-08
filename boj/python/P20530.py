# C번 - 양분
# https://www.acmicpc.net/contest/problem/578/3
# https://www.acmicpc.net/problem/20530
# Not solved
from sys import stdin

N, Q = map(int, input().split())
G: list = [list() for _ in range(N + 1)]
for _ in range(N):
    a, b = map(int, stdin.readline().split())
# DFS 쓰는건가?
for edge in stdin.readlines():
    a, b = map(int, edge.split())
    visited: set = set()
    stack = [a]
    count = 0
    while stack:
        n = stack.pop()
        # if n not in visited:
        #     visited.add(n)
