# https://school.programmers.co.kr/learn/courses/30/lessons/468370
# 2026-07-08 / 2025 카카오 하반기 1차 > 중요한 단어를 스포 방지 / Lv. 1


# 문제 풀이 접근 방법
# 1. 일단 스포방지 걸린 단어와 안걸린 단어를 분류
# 2. 스포 방지가 걸린 단어 목록에만 있는 스포방지 단어의 갯수를 반환

# [1]은 단순하게 한 글자씩 인덱스를 올려가며 단어의 시작·끝지점, 스포일러 여부와 단어의 스포일러 여부 상태 등을 관리
#   좋은 코드는 아니라고 생각된다.
# [2]는 깔끔하게 파이썬의 set() 자료형에서 제공하는 차집합 기능을 사용


def solution(message: str, spoiler_ranges: list[list[int]]) -> int:
    is_spoiler = False
    is_spoiler_word = False
    spoiler_set = set()
    non_spoiler_set = set()
    spoiler_index = 0
    spoiler_start, spoiler_end = spoiler_ranges[spoiler_index]
    word_start = 0
    for i in range(len(message)):
        if i == spoiler_start:
            is_spoiler = True
            is_spoiler_word = True

        if i > 0 and message[i - 1] == " ":
            word_start = i
            is_spoiler_word = is_spoiler
        if i == len(message) - 1 or message[i + 1] == " ":
            if is_spoiler_word:
                spoiler_set.add(message[word_start : i + 1])
            else:
                non_spoiler_set.add(message[word_start : i + 1])
            is_spoiler_word = False

        if i == spoiler_end:
            is_spoiler = False
            spoiler_index = min(spoiler_index + 1, len(spoiler_ranges) - 1)
            spoiler_start, spoiler_end = spoiler_ranges[spoiler_index]

    return len(spoiler_set - non_spoiler_set)


if __name__ == "__main__":
    print(
        solution(
            "here is muzi here is a secret message",
            [[0, 3], [23, 28]],
        )
    )
    print(
        solution(
            "my phone number is 01012345678 and may i have your phone number",
            [[5, 5], [25, 28], [34, 40], [53, 59]],
        )
    )
