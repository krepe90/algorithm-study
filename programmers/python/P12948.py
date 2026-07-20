# https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 2026-07-20 / 연습문제 > 핸드폰 번호 가리기 / Lv. 1
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열


def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]
