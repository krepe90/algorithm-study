# https://www.acmicpc.net/problem/10814
from sys import stdin
N = int(input())
A = [stdin.readline().split() for _ in range(N)]
A.sort(key=lambda x: int(x[0]))
print("\n".join(f"{n[0]} {n[1]}" for n in A))
