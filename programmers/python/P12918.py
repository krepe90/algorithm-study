# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 2026-07-19 / 연습문제 > 문자열 다루기 기본 / Lv. 1
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열


def solution(s: str):
    return s.isdigit() and len(s) in (4, 6)
