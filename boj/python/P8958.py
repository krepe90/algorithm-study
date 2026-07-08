# https://www.acmicpc.net/problem/8958
T = int(input())
for i in range(T):
    X = input()
    r, s = 0, 0
    for c in X:
        if c == "O":
            s += 1
            r += s
        else:
            s = 0
    print(r)
