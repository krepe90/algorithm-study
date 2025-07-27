# https://www.acmicpc.net/problem/28125
# 2025-07-27 / 28125. 2023 아주머학교 프로그래딩 정시머힌 / Silver IV

m = [
    ("w", "\\\\'"),
    ("v", "\\'"),
    ("a", "@"),
    ("c", "["),
    ("i", "!"),
    ("j", ";"),
    ("n", "^"),
    ("o", "0"),
    ("t", "7"),
]

T = int(input())

for _ in range(T):
    s = input()

    cnt = 0
    for o, r in m:
        cnt += s.count(r)
        s = s.replace(r, o)

    if cnt >= len(s) / 2:
        print("I don't understand")
    else:
        print(s)
