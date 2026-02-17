# https://www.acmicpc.net/problem/7326
# 2026-02-17 / 7326. Number Steps / Bronze I

# (0, 0) 시작, 0
# (1, 1) 시작, 1
# (2, 0) 시작, 2
# (3, 1) 시작, 3
# 이후 각각 좌표에 2씩 더하기 / 값에 4씩 더하기

for _ in range(int(input())):
    x, y = map(int, input().split())
    a = y // 2
    if x == y:
        if x % 2 == 0:
            print(a * 4)
        else:
            print(a * 4 + 1)
    elif x - y == 2:
        if x % 2 == 0:
            print(a * 4 + 2)
        else:
            print(a * 4 + 3)
    else:
        print("No Number")
