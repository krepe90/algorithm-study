# https://www.acmicpc.net/problem/2753
x = int(input())
print(0 if x % 400 and (x % 4 or not x % 100) else 1)
