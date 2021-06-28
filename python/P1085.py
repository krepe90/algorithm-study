# https://www.acmicpc.net/problem/1085
# 6, 2에 있고 10, 3이 꼭지점.
X, Y, W, H = map(int, input().split())
print(min((abs(X - W), abs(Y - H), X, Y)))
