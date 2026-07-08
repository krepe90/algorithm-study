# Good Bye, BOJ!
# A번 - Good Bye, 별 찍기!
# https://www.acmicpc.net/contest/problem/1675/1

# / 모양 대각선으로 별, 공백 1줄, 다이아몬드 모양
# 0..2N 인 i일 때 각 줄마다:
#   1. (2N-i-1)개의 공백 후 별
#   2. 1개의 공백
#   3. ...
# 0, 1, 2, 2, 1, 0

N = int(input())

for i in range(0, 2 * N):
    print(" " * (2 * N - i - 1) + "*" + " " * i, end=" ")
    j = i if i < N else N - (i % N) - 1
    print(" " * (N - j - 1) + "*" + " " * j, end=" ")
    print(" " * j + "*" + " " * (N - j - 1))
