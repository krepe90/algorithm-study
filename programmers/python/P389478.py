# https://school.programmers.co.kr/learn/courses/30/lessons/389478
# 2026-07-09 / 2025 프로그래머스 코드챌린지 2차 예선 / 택배 상자 꺼내기

# n <= 100 이라서 그냥 2차원 배열같은거 만들어서 그거 돌려도 되지 않을까
# 입출력은 1-based index인 것에 유의

# 좀 더 수학적으로 깔끔한 방법이 있을텐데 그 방법을 떠올리지 못하고 공간복잡도 좀 높여서 해결한건 조금 아쉬운 부분


def solution(n: int, w: int, num: int):
    boxes: list[set[int]] = [set() for _ in range(w)]
    for i in range(n):
        box_index = i % w
        if (i // w) % 2:  # if is odd
            boxes[-box_index - 1].add(i + 1)
        else:
            boxes[box_index].add(i + 1)
    for col in boxes:
        if num in col:
            return sum(1 for x in col if x >= num)


if __name__ == "__main__":
    print(solution(22, 6, 8))
    print(solution(13, 3, 6))
