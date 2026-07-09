# https://school.programmers.co.kr/learn/courses/30/lessons/468371
# 2026-07-09 / 2025 카카오 하반기 1차 > 노란불 신호등 / Lv. 1

# G, Y, R 값이나 신호등 갯수가 작으니까 전부 다 연산하기
# 좀 더 효율적으로 연산하는 방법도 있긴 하겠지만 크게 중요하진 않은 부분
# - is_y 함수에서 매번 전체 사이클 길이인 c 값을 구하는 부분이라던지

# 다른 사람들 코드 보고 있는데 나는 좀 파이싸닉하게 잘 짠듯
# 다르게 말하면 뇌가 파이썬에 절여진거 아닌가...
# 생각해보니까 저 작은 함수는 is_y 라는 이름이 더 좋을 것 같아서 바꿈

import math


def is_y(g, y, r, t) -> bool:
    c = g + y + r
    return g < (t % c) <= g + y


def solution(signals: list[list[int]]):
    total = math.lcm(*(sum(a) for a in signals))
    for t in range(1, total + 1):
        if all(is_y(*a, t) for a in signals):
            return t
    return -1


if __name__ == "__main__":
    print(solution([[2, 1, 2], [5, 1, 1]]))
    print(solution([[2, 3, 2], [3, 1, 3], [2, 1, 1]]))
    print(solution([[3, 3, 3], [5, 4, 2], [2, 1, 2]]))
    print(solution([[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]))
