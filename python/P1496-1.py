# https://www.acmicpc.net/contest/problem/1496/1
# A번 - 아깝게 놓친 COSS 장학금


"""
장학 점수가 높은 학생이 먼저 오도록 내림차순으로 정렬한다.
장학 점수가 동일한 학생들이 있는 경우, 프로젝트 진행 비용이 적은 학생이 먼저 오도록 오름차순으로 정렬한다.
장학 점수와 프로젝트 진행 비용이 모두 동일한 학생들이 있는 경우, 이름이 사전 순으로 빠른 학생이 먼저 오도록 정렬한다.
"""

n = int(input())
arr = []
for _ in range(n):
    name, *s = input().split()
    score, risk, cost = map(int, s)
    gs = int(score ** 3 / (cost * (risk + 1)))

    arr.append(
        (-gs, cost, name)
    )

arr.sort()
print(arr[1][2])
