# https://school.programmers.co.kr/learn/courses/30/lessons/77485
# 2026-07-13 / 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 행렬 테두리 회전하기 / Lv. 2
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 3장. 배열

# 1. 회전시켜야 하는 좌표들을 전부 list[tuple[int, int]] 로 만들고
# 2. list comp로 해당 좌표의 값들을 구한 다음
# 3. 반복문으로 하나씩 밀어서 (중요) 값을 대입
# 4. 끝날때까지 [1]을 반복

# 난 아무래도 (y, x) 로 쓰고 [y][x] 로 접근하는게 더 익숙한 것 같다...
# 이게 다 opencv 때문이야
# get_coords 함수를 좀 더 예쁘게 쓸 수 있지 않았을까?

# 나중에 봤는데 이해 못할까봐 보충설명
# 0 1 2
# 5 4 3
# 이렇게 6개 칸이 회전해야 할 때 n번째 index의 (y, x) 에다가 n-1 번째 기존값을 대입하는 방식으로 회전을 구현
# arr_coord index:   0 1 2 3 4 5
# rotate_val index: -1 0 1 2 3 4
# 이 때 파이썬 리스트의 특성상 -1은 마지막 원소인 5로 해석되며, [5 0 1 2 3 4] 가 돼 의도대로 시계방향으로 회전한다.
# -1 0 1  ->  5 0 1
#  4 3 2      4 3 2


def get_coords(y1: int, x1: int, y2: int, x2: int) -> list[tuple[int, int]]:
    coords = []
    for x in range(x1, x2):
        coords.append((y1, x))
    for y in range(y1, y2):
        coords.append((y, x2))
    for x in range(x2, x1, -1):
        coords.append((y2, x))
    for y in range(y2, y1, -1):
        coords.append((y, x1))
    return coords


def solution(rows: int, columns: int, queries: list[list[int]]):
    arr = [[y * columns + x + 1 for x in range(columns)] for y in range(rows)]
    answer = []
    for q in queries:
        coords = get_coords(*q)
        rotate_values = list(arr[y - 1][x - 1] for y, x in coords)
        answer.append(min(rotate_values))
        for i, (y, x) in enumerate(coords):
            arr[y - 1][x - 1] = rotate_values[i - 1]
    return answer


if __name__ == "__main__":
    print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
    print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
    print(solution(100, 97, [[1, 1, 100, 97]]))
