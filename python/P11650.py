# https://www.acmicpc.net/problem/11650
from sys import stdin
N = int(input())
A = sorted([tuple(map(int, stdin.readline().split())) for _ in range(N)])
print("\n".join(f"{n[0]} {n[1]}" for n in A))
