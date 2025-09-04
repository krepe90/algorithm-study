# https://www.acmicpc.net/problem/1837
# 2025-09-04 / 1837. 암호제작 / Bronze III

P, K = map(int, input().split())
for i in range(2, K):
    if P % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")
