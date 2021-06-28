# https://www.acmicpc.net/problem/2562
M = 0
for i in range(1, 10):
    x = int(input())
    if M < x:
        M = x
        k = i
print(M)
print(k)
