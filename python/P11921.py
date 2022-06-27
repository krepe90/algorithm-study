# https://www.acmicpc.net/problem/11921

import sys
n = int(sys.stdin.readline())
print(n)
print(sum(map(int, (sys.stdin.readline() for _ in range(n)))))
# print(n * (n + 1) / n)
