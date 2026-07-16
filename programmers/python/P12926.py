# https://school.programmers.co.kr/learn/courses/30/lessons/12926
# 2026-07-16 / 연습문제 > 시저 암호 / Lv. 1
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열

# 알파벳을 뒤로 한 글자씩 밀어주면 된다. 이 때 대소문자는 유지한다
# 간단하게 shift 함수를 만들어서 처리해주면 될듯
# n을 넣어줘야 해서 map 함수를 못쓴게 좀 아쉬운 부분 (이거 해결방법이 있긴 한데 까먹었다.)


def shift(c: str, n: int) -> str:
    if c == " ":
        return c
    x = 65 if ord(c) <= 90 else 97
    return chr((ord(c) - x + n) % 26 + x)


def solution(s, n):
    return "".join(shift(c, n) for c in s)


if __name__ == "__main__":
    print(solution("AB", 1))
    print(solution("z", 1))
    print(solution("a B z", 4))
