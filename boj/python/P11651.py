# https://www.acmicpc.net/problem/11651
from sys import stdin
N = int(input())
A = sorted([tuple(map(int, stdin.readline().split()[::-1])) for _ in range(N)])
print("\n".join(f"{n[1]} {n[0]}" for n in A))
