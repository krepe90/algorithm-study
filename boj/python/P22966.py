# https://www.acmicpc.net/problem/22966
# 2025-07-11 / 22966. 가장 쉬운 문제를 찾는 문제 / Bronze II

N = int(input())
p_list: list[tuple[int, str]] = []
for _ in range(N):
    name, rate = input().split()
    p_list.append((int(rate), name))
p_list.sort()
print(p_list[0][1])

