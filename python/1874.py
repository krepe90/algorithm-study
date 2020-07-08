# https://www.acmicpc.net/problem/1874
import sys
N = int(input())
NUM = iter(range(1, N + 1))
A = []
R = []

try:
    for i in range(N):
        x = int(sys.stdin.readline())
        while not A or A[-1] != x:
            R.append("+")
            A.append(next(NUM))
        A.pop()
        R.append("-")
except StopIteration:
    print("NO")
else:
    print("\n".join(R))
