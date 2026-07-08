# https://www.acmicpc.net/problem/4732
# 2025-07-24 / 4732. 조옮김 / Bronze I

# 일단 정규화(?)를 한 다음에 계산을 하면 되지 않나
a = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def conv(t: str, d=0):
    if t in a:
        i = a.index(t) + d
    else:
        c, op = t
        i = a.index(c)
        i = i + d + 1 if op == "#" else i + d - 1
    return a[i % 12]


while (s := input()) != "***":
    delta = int(input())
    print(*[conv(t, delta) for t in s.split()])
