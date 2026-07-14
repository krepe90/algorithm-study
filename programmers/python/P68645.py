# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 2026-07-14 / 월간 코드 챌린지 시즌1 > 삼각 달팽이 / Lv. 2
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 3장. 배열

#     1
#    2 C
#   3 D B
#  4 E F A
# 5 6 7 8 9

# 규칙을 찾는게 핵심인 문제
# 꺾이면서 길이가 5,4,3,2,1 이 된다
# 저걸 1차원 배열이라고 생각하면 idx 증감폭이
#   case 1: 0, 1, 3, 6, 10
#   case 2: 11, 12, 13, 14
#   case 3: (14,) 9, 5, 2
# 두 규칙을 잘 섞어서 뺑뺑이 돌리면 될듯

# 뭔가 더 깔끔한 해결법 없었을까


def solution(n):
    answer = [-1] * (n * (n + 1) // 2)
    i = 0
    mode = 1
    current_row = 1  # 1부터 시작
    total_len = len(answer)
    for val in range(1, (n * (n + 1) // 2) + 1):
        answer[i] = val

        if mode == 1 and (current_row >= n or answer[i + current_row] != -1):
            mode = 2
        if mode == 2 and (i + 1 >= total_len or answer[i + 1] != -1):
            mode = 3
        if mode == 3 and (current_row < 1 or answer[i - current_row] != -1):
            mode = 1

        if mode == 1:
            i += current_row
            current_row += 1
        elif mode == 2:
            i += 1
        elif mode == 3:
            i -= current_row
            current_row -= 1

    return answer


if __name__ == "__main__":
    print(solution(4))
    print(solution(5))
    print(solution(6))
