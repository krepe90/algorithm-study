# A번 - 끝말잇기
# https://www.acmicpc.net/contest/problem/578/1
# https://www.acmicpc.net/problem/20528
# Solved
N: int = int(input())
S: list = [n for n in input().split()]
w = S[0][0]
for word in S:
    if w != word[0]:
        print(0)
        break
else:
    print(1)
