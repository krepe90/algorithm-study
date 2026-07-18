# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 2026-07-18 / 2017 팁스타운 > 짝지어 제거하기 / Lv. 2
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열

# 순서가 중요한 케이스가 있을 수 있나?
# 곰곰히 생각해봤는데 어지간해선 없을듯
# 일단은 괄호열기닫기 느낌이니까 스택으로 풀면 될 것 같긴 하다.


def solution(s: str):
    stack = []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()

    return 0 if stack else 1
