# https://www.acmicpc.net/problem/2475
print(sum(n * n for n in map(int, input().split())) % 10)
