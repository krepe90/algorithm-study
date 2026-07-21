# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 2026-07-21 / 2020 KAKAO BLIND RECRUITMENT > 문자열 압축 / Lv. 2
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열

# a -> a
# aa -> 2a
# aaa -> 3a

# len(s)가 1인 경우를 생각을 못했다.
# range 범위를 [1, n // 2 + 1) 로 표현을 했는데, n = 1이면 [1, 1) 이 되어 반복문을 아예 돌지 않고 1000을 반환한다
# 절반 정도만 돌도록 했던 것은 최적화를 위하여 추가한 부분이고 로직상 중요한 부분은 아니였기 때문에 +1 해주던 부분을 +2로 변경하여 해결하였다.
# 테케 딱 하나만 틀리더라...


def min_len(s: str, n: int):
    """n개의 문자열 s를 표현할 때의 최소 길이"""
    # print(min(s * n, f"{n}{s}", key=len), end="")
    return min(len(s) * n, len(s) + len(str(n)))


def c(s: str, n: int):
    total = 0
    combo = 0
    prev = ""
    for i in range(0, len(s), n):
        w = s[i : i + n]
        if w != prev:
            total += min_len(prev, combo)
            combo = 1
        else:
            combo += 1
        prev = w
    else:
        total += min_len(prev, combo)
    # print(f" -> {total}")
    return total


def solution(s):
    answer = 1000
    for n in range(1, len(s) // 2 + 2):
        answer = min(answer, c(s, n))
    return answer


if __name__ == "__main__":
    print(solution("aabbaccc"))
    print(solution("ababcdcdababcdcd"))
    print(solution("abcabcdede"))
    print(solution("abcabcabcabcdededededede"))
    print(solution("xababcdcdababcdcd"))

    print(solution("a"))
