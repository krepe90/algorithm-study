# https://www.acmicpc.net/problem/10989
# 수 정렬하기 3 - Bronze 1

import array
import sys
sin = sys.stdin.readline
sout = sys.stdout.write
a = array.array("I", (0 for _ in range(10001)))
for _ in range(int(sin())):
    a[int(sin())] += 1
for i, n in enumerate(a):
    s = str(i) + "\n"
    for _ in range(n):
        sout(s)
