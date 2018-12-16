# Solved
# https://www.acmicpc.net/problem/10430


# Solution 1
val = input().split(" ")
a, b, c = list(map(int, val))
print(f"{(a + b) % c}\n{(a % c + b % c) % c}\n{(a * b) % c}\n{(a % c * b % c) % c}")
