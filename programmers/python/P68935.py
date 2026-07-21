# https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 2026-07-21 / 월간 코드 챌린지 시즌1 > 3진법 뒤집기 / Lv. 1
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열

# 파이썬의 int에는 base= 라는 파라미터가 있어서 n진수를 10진수로 편하게 바꿀 수 있다
# 평소에는 쓸 일이 없고 PS할때나 쓰는 기능이지만 ㅎㅎ;;


def solution(n):
    arr = []
    while n:
        arr.append(n % 3)
        n //= 3
    return int("".join(map(str, arr)), base=3)


if __name__ == "__main__":
    print(solution(45))
    print(solution(125))
