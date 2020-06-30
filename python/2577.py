# https://www.acmicpc.net/problem/2577
A, B, C = map(int, (input(), input(), input()))
x = str(A * B * C)
for i in range(0, 10):
    print(x.count(str(i)))
