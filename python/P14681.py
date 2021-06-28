# https://www.acmicpc.net/problem/14681
X, Y = int(input()), int(input())
print([[1, 4], [2, 3]][0 if X > 0 else 1][0 if Y > 0 else 1])
