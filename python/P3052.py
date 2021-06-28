# https://www.acmicpc.net/problem/3052
x = set()
for i in range(10):
    x.add(int(input()) % 42)
print(len(x))
