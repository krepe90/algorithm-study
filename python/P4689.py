# https://www.acmicpc.net/problem/4689
# 2025-07-25 / 4689. Basically Speaking / Silver V


d = "0123456789ABCDEF"


def conv(n: int, b: int) -> str:
    arr = []
    while n:
        arr.append(n % b)
        n = n // b
    return "".join(d[i] for i in arr[::-1])


while True:
    try:
        _n, _b_from, _b_to = input().split()
    except Exception:
        break

    n = int(_n, int(_b_from))
    s = conv(n, int(_b_to))

    if len(s) > 7:
        s = "ERROR"

    print(f"{s:>7}")
