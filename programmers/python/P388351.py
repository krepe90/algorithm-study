# https://school.programmers.co.kr/learn/courses/30/lessons/388351
# 2026-07-10 / 2025 프로그래머스 코드챌린지 1차 예선 > 유연근무제 / Lv. 1

# 일찍 출근하는건 딱히 상관 없고 딱 두개만 고민하면 된다
# 출근 인정시간보다 같거나 빠른가, 평일인가
# 1. 인정시간 배열을 만들어서 비교하면됨
# 2. 날짜를 계산하는 방법을 생각해보기. 0123456 + startday - 1 하면 shift가 되고, mod 7 해주면

# mod 7 까먹어서 틀렸다 어이없
# 너무 코드가 쓸데없이 복잡하게 짜여진거 아닌가?


def add_time(i: int) -> int:
    h, m = i // 100, i % 100
    m += 10
    if m > 59:
        h, m = h + 1, m % 60
    return h * 100 + m


def solution(schedules: list[int], timelogs: list[list[int]], startday: int):
    limits = [add_time(n) for n in schedules]

    results = [
        all(arr[j] <= limits[i] for j in range(7) if (j + startday - 1) % 7 < 5)
        for i, arr in enumerate(timelogs)
    ]
    return results.count(True)


if __name__ == "__main__":
    print(
        solution(
            [700, 800, 1100],
            [
                [710, 2359, 1050, 700, 650, 631, 659],
                [800, 801, 805, 800, 759, 810, 809],
                [1105, 1001, 1002, 600, 1059, 1001, 1100],
            ],
            5,
        )
    )
    print(
        solution(
            [730, 855, 700, 720],
            [
                [710, 700, 650, 735, 700, 931, 912],
                [908, 901, 805, 815, 800, 831, 835],
                [705, 701, 702, 705, 710, 710, 711],
                [707, 731, 859, 913, 934, 931, 905],
            ],
            1,
        )
    )
