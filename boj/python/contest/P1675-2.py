# Good Bye, BOJ!
# B번 - Good Bye, 설탕 배달!
# https://www.acmicpc.net/contest/problem/1675/2

# p_i 에 대해서, 현재 a,b,c에 대해 추가로 필요한 스탯을 계산한 뒤 잉여분을 계산해 더하거나 종료하거나
# 어째서 시간초과인걸까 -> 보통 IO이슈
# 근데 이걸로도 해결 안돼서 그냥 PyPy3 치트키를 사용했다. 흠...

import sys

input = lambda: sys.stdin.readline().rstrip()


for _ in range(int(input())):
    N = int(input())
    a, b, c, solved = 0, 0, 0, 0

    ok = True
    for i in range(N):
        a_i, b_i, c_i, p_i = map(int, input().split())
        req_a = a_i - a if a_i > a else 0
        req_b = b_i - b if b_i > b else 0
        req_c = c_i - c if c_i > c else 0

        if not ok or (req_a + req_b + req_c) > p_i - (a + b + c + solved) - 1:
            ok = False
            continue
        a += req_a
        b += req_b
        c += req_c
        solved += 1
    else:
        print("YES")
