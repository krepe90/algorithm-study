# https://www.acmicpc.net/problem/28702
# FizzBuzz

for i in range(3):
    N = input()
    if N.isdigit():
        R = int(N) + (3 - i)
print(R)
