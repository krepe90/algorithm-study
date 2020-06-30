# https://www.acmicpc.net/problem/1546
N = int(input())
X = list(map(int, input().split()))
M = max(X)
print(sum(i / M * 100 for i in X) / N)
