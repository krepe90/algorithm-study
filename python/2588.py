# https://www.acmicpc.net/problem/2588
A = int(input())
B = int(input())
print(A * (B % 10))
print(A * (B % 100 - B % 10) // 10)
print(A * (B % 1000 - B % 100) // 100)
print(A * B)
