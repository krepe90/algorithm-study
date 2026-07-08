# Solved
# https://www.acmicpc.net/problem/10869


# Solution 1
val = input().split(" ")
a, b = int(val[0]), int(val[1])
print(f"{a+b}\n{a-b}\n{a*b}\n{int(a/b)}\n{a%b}")
