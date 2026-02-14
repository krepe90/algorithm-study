# https://www.acmicpc.net/problem/14626
# 2026-02-14 / 14626. ISBN / Bronze I
# CLASS 2++


# 이딴식으로 풀어도 되는걸까?


def isbn(s: str) -> bool:
    a, b, c, d, e, f, g, h, i, j, k, l, m = map(int, s)
    return (
        a + 3 * b + c + 3 * d + e + 3 * f + g + 3 * h + i + 3 * j + k + 3 * l + m
    ) % 10 == 0


s = input()
for i in range(10):
    s_ = s.replace("*", str(i))
    if isbn(s_):
        print(i)
        break
