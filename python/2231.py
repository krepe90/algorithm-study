# https://www.acmicpc.net/problem/2231
import math
N = int(input())
for i in range(N - (int(math.log10(N)) + 1) * 9, N):
    if i < 1:
        continue
    # 분해합 구하는 코드
    s, x = i, i
    while x:
        s += x % 10
        x //= 10
        # print(x)
    if s == N:
        print(i)
        break
else:
    print(0)
