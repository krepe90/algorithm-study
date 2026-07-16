# https://school.programmers.co.kr/learn/courses/30/lessons/12949
# 2026-07-16 / 연습문제 > 행렬의 곱셈 / Lv. 2
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 3장. 배열

# 저 numpy 쓰고싶어요
# 행렬곱... 어떻게 구현해야 하지

# 1. 행렬의 곱이란?
# m*n 행렬 A랑 n*p 행렬 B 의 행과 열끼리 곱한걸 더해서 m*p 크기의 새 행렬을 만드는거
# 2. 구현 방법은
# 2-1. 일단 mnp 값들을 먼저 구하고
# 2-2. 곱할 행과 열 (== 새 행렬의 좌표값이 될) 의 이중 반복문을 돌리고
# 2-3. A의 행과 B의 열 곱하고 더하고 해주기

# 설명 진짜 못한다.


def solution(arr1, arr2):
    m, n = len(arr1), len(arr1[0])
    p = len(arr2[0])
    answer = [[-1] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            answer[i][j] = sum(arr1[i][k] * arr2[k][j] for k in range(n))
    return answer


if __name__ == "__main__":
    print(
        solution(
            [
                [1, 4],
                [3, 2],
                [4, 1],
            ],
            [
                [3, 3],
                [3, 3],
            ],
        )
    )
    print(
        solution(
            [
                [2, 3, 2],
                [4, 2, 4],
                [3, 1, 4],
            ],
            [
                [5, 4, 3],
                [2, 4, 1],
                [3, 1, 1],
            ],
        )
    )
