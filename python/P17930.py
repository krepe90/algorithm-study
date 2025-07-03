# https://www.acmicpc.net/problem/17930
# 2025-07-03 / 17930. Hanging Out on the Terrace / Bronze II

L, x = map(int, input().split())
current = 0
denied = 0
for _ in range(x):
    event, s_people = input().split()
    people = int(s_people)
    if event == "enter":
        if current + people > L:
            denied += 1
        else:
            current += people
    else:
        current -= people
print(denied)
