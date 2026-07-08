# https://www.acmicpc.net/problem/2979
# 2025-07-10 / 2979. 트럭 주차 / Bronze II

# approach A. 1차원 시계열로 만들고 시간대별 계산해서 출력
# approach B. (i, o) 로 영역을 나누고, 겹치는 부분들을 새로 계산하여 만들기
# approach C. 그냥 1부터 100까지 전부 계산

A, B, C = map(int, input().split())
t = [0] * 101
for _ in range(3):
    it, ot = map(int, input().split())
    for i in range(it, ot):
        t[i] += 1
prices = [0, A, B * 2, C * 3]
answer = 0
for p in t:
    answer += prices[p]
print(answer)
