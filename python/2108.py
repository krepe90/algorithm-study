# https://www.acmicpc.net/problem/2108
from sys import stdin
N = int(input())
A = [int(stdin.readline()) for _ in range(N)]
A.sort()

# 합, 중앙값, 최빈값, 범위
s = 0
med = A[N >> 1]
freq_d = {}
rng = A[-1] - A[0]
for i in A:
    s += i
    freq_d[i] = freq_d.get(i, 0) + 1
freq = sorted(zip(freq_d.values(), freq_d.keys()), reverse=True, key=lambda x: (x[0], -x[1]))
if len(freq) > 1 and freq[0][0] == freq[1][0]:
    f = freq[1][1]
else:
    f = freq[0][1]

print(round(s / N))
print(med)
print(f)
print(rng)
