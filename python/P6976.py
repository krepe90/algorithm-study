# https://www.acmicpc.net/problem/6976
# 2025-07-23 / 6976. Divisibility by 11 / Bronze II

T = int(input())
for _ in range(T):
    s = s_ = input()
    while len(s) > 2:
        print(s)
        s = str(int(s[:-1]) - int(s[-1]))
    print(s)

    is_ = "is" if s == "11" else "is not"
    print(f"The number {s_} {is_} divisible by 11.\n")
