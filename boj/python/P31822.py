# https://www.acmicpc.net/problem/31822
# 2025-08-20 / 31822. 재수강 / Bronze IV

code = input()[:5]
# print(sum(int(input().startswith(code)) for _ in range(int(input()))))
print(sum(1 for _ in range(int(input())) if input().startswith(code)))
