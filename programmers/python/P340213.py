# https://school.programmers.co.kr/learn/courses/30/lessons/340213
# 2026-07-11 / PCCP 기출문제 > [PCCP 기출문제] 1번 / 동영상 재생기 / Lv. 1


# 그냥 단순 구현문제
# 문자열로 들어온 타임스탬프를 초 단위로 바꾸어 간결하게 처리하는게 좋아보인다.
# match 함수를 쓰는게 좋았으려나?


def s2i(s: str) -> int:
    return int(s[0:2]) * 60 + int(s[3:5])


def i2s(i: int) -> str:
    return f"{i // 60:02d}:{i % 60:02d}"


def solution(video_len: str, pos: str, op_start: str, op_end: str, commands: list[str]):
    vl, p, os, oe = map(s2i, [video_len, pos, op_start, op_end])
    for c in commands:
        # 오프닝 건너뛰기
        if os <= p <= oe:
            p = oe
        # prev/next 명령
        if c == "prev":
            p -= 10
        elif c == "next":
            p += 10
        # 정규화 (재생시간 초과/미만, 오프닝)
        if p < 0:
            p = 0
        if p > vl:
            p = vl
        if os <= p <= oe:
            p = oe  # 이게 없으면 마지막 명령에서 오프닝 구간으로 진입했을 때의 처리가 제대로 안될거임
    return i2s(p)
