# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 2026-07-17 / 연습문제 > 이상한 문자 만들기 / Lv. 1
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열

# 아무리 급하더라도 문제는 천천히, 꼼꼼히 읽도록 하자...


def solution(s):
    answer_list = []
    is_even = True
    for c in s:
        if c == " ":
            answer_list.append(c)
            is_even = True
        elif is_even:
            answer_list.append(c.upper())
            is_even = False
        else:
            answer_list.append(c.lower())
            is_even = True
    return "".join(answer_list)


if __name__ == "__main__":
    print(solution("try hello world"))
