# Unsolved
# https://www.acmicpc.net/problem/1463

x = int(input())
c = 0

while x != 1:
    if x % 3 == x % 2 == 0:
        if x % 3 == 0:
            x /= 3
    else:
        x -= 1
    c += 1
    print(x)
print(c)
