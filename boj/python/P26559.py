# https://www.acmicpc.net/problem/26559
# 2025-06-29 / 26559. Friends / Silver V

n = int(input())
for _ in range(n):
    m = int(input())
    arr = []
    for _ in range(m):
        name, num_s = input().split()
        num = int(num_s)
        arr.append((num, name))
    arr.sort(reverse=True)
    print(*(b for a, b in arr), sep=", ")
