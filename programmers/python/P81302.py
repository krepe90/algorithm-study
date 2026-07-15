# https://school.programmers.co.kr/learn/courses/30/lessons/81302
# 2026-07-15 / 2021 카카오 채용연계형 인턴십 > 거리두기 확인하기 / Lv. 2


def c(p: list[str], y: int, x: int):
    """안전하게 값 구하기"""
    if not (0 <= y < 5 and 0 <= x < 5):
        return ""
    return p[y][x]


def check_cell(p: list[str], y: int, x: int):
    """하나라도 문제 있으면 False 반환"""
    case_1 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    case_2 = [
        # case 2-1
        [(1, 0), (2, 0)],
        [(0, 1), (0, 2)],
        [(-1, 0), (-2, 0)],
        [(0, -1), (0, -2)],
        # case 2-2
        [(1, 0), (1, 1)],
        [(1, 0), (1, -1)],
        [(-1, 0), (-1, 1)],
        [(-1, 0), (-1, -1)],
        [(0, 1), (1, 1)],
        [(0, 1), (-1, 1)],
        [(0, -1), (1, -1)],
        [(0, -1), (-1, -1)],
    ]
    for dy, dx in case_1:
        if c(p, y + dy, x + dx) == "P":
            return False
    for (dy1, dx1), (dy2, dx2) in case_2:
        if c(p, y + dy1, x + dx1) == "O" and c(p, y + dy2, x + dx2) == "P":
            return False
    return True


def check_place(p: list[str]):
    for y in range(5):
        for x in range(5):
            if p[y][x] == "P":
                is_ok = check_cell(p, y, x)
                if not is_ok:
                    return 0
    return 1


def solution(places: list[list[str]]):
    answer = [check_place(p) for p in places]
    return answer


if __name__ == "__main__":
    print(
        solution(
            [
                ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
            ]
        )
    )
