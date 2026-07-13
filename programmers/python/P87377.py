# https://school.programmers.co.kr/learn/courses/30/lessons/87377
# 2026-07-13 / 위클리 챌린지 > 교점에 별 만들기 / Lv. 2
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 3장. 배열

# 어째서인지 2024-05-31 새벽 6시에 (...) 풀었던 기록이 있다.

# 1. 정수인 교점을 구하고
# 2. [1]의 최소/최대 구간을 구해
#    해당 구간 내에서 교점이면 별, 아니면 온점이 되게 문자열을 만들어 출력

import itertools


def solution(line: list[list[int]]):
    combi = itertools.combinations(line, 2)
    points = []

    # 정수인 교점 찾기
    for (a, b, e), (c, d, f) in combi:
        if (a * d - b * c) == 0:
            continue
        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)
        if x.is_integer() and y.is_integer():
            points.append((int(y), int(x)))

    # 교점 정렬
    points.sort()
    y_min, y_max = points[0][0], points[-1][0]
    x_min, x_max = min(x for y, x in points), max(x for y, x in points)
    answer = [
        "".join("*" if (y, x) in points else "." for x in range(x_min, x_max + 1))
        for y in range(y_min, y_max + 1)[::-1]
    ]
    return answer


if __name__ == "__main__":
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
    print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
    print(solution([[1, -1, 0], [2, -1, 0]]))
    print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
