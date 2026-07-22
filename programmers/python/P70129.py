# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 2026-07-22 / 월간 코드 챌린지 시즌1 > 이진 변환 반복하기 / Lv. 1
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열

# 원래는 [이진 변환] 함수를 만들었는데, 이러면 제거한 0의 갯수를 반환하기가 조금 골룸해진다.


def bc(x: str) -> tuple[str, int]:
    orig_len = len(x)
    x = x.replace("0", "")
    return f"{len(x):b}", orig_len - len(x)


def solution(s):
    total, i = 0, 0
    while s != "1":
        s, removed = bc(s)
        i += 1
        total += removed
    return [i, total]


if __name__ == "__main__":
    print(solution("110010101001"))
    print(solution("01110"))
    print(solution("1111111"))
