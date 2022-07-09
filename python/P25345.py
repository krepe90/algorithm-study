# https://www.acmicpc.net/problem/25345
# https://www.acmicpc.net/contest/problem/838/1
# Semi-Game Cup 3
# A번 - 루나의 게임 세팅

# nCk * 2^(k-1)
P = 10 ** 9 + 7


d = [[1], [1, 1]]
for i in range(2, 2001):
    d.append([1] + [(d[-1][n - 1] + d[-1][n]) % P for n in range(1, i)] + [1])


n, k = map(int, input().split())
_ = input()

# # 1. nCk 구하기
result = d[n][k]

# # 2. 2^(k-1) 구하기
result *= pow(2, k - 1, P)
result %= P
print(result)
