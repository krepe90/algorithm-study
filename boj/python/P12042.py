# https://www.acmicpc.net/problem/12042
# 2025-07-08 / 12042. Lazy Spelling Bee (Small) / Silver IV

T = int(input())
for x in range(1, T + 1):
    W = input()
    answer = 1
    for i in range(len(W)):
        s = i - 1 if i else 0
        answer *= len(set(W[s:i+2]))
    print(f"Case #{x}: {answer}")
