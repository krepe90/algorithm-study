# https://www.acmicpc.net/problem/10039
S = [int(input()) for n in range(5)]
print(sum(n if n > 40 else 40 for n in S) // 5)
