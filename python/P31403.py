# https://www.acmicpc.net/problem/31403
# A + B - C

a, b, c = map(int, [input() for _ in range(3)])
print(a + b - c)
print(int(f"{a}{b}") - c)
